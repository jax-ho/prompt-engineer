#!/usr/bin/env python3
"""Contract tests for the prompt-engineer skill."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = SKILL_ROOT.parents[1]
SKILL = SKILL_ROOT / "SKILL.md"
README = REPO_ROOT / "README.md"
ORDINARY = SKILL_ROOT / "references" / "prompt-optimizer-meta-prompt.md"
AGENT = SKILL_ROOT / "references" / "agent-prompt-optimizer-meta-prompt.md"
CHECKLIST = SKILL_ROOT / "references" / "quality-checklist.md"
EXAMPLES = SKILL_ROOT / "examples" / "requests.md"
CASES = SKILL_ROOT / "tests" / "cases.json"

AGENT_ROUTE_TERMS = [
    "agent",
    "ReAct",
    "tool-use",
    "function-calling",
    "tool-schema",
    "MCP",
    "browser/file/code-execution",
    "API",
    "retrieval",
    "observation-based",
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    assert_true(lines[:1] == ["---"], "SKILL.md must start with YAML frontmatter")
    end = lines.index("---", 1)
    data: dict[str, str] = {}
    for line in lines[1:end]:
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()
    return data


def fence_lines(text: str) -> list[int]:
    return [idx + 1 for idx, line in enumerate(text.splitlines()) if line.strip().startswith("```")]


def routed_by_test_oracle(request: str) -> str:
    """A narrow route oracle matching the skill's explicit trigger policy."""
    lower = request.lower()

    # Ordinary explanatory prompts can mention API/tool concepts without asking for agent behavior.
    ordinary_explanations = [
        "what an api is",
        "what a tool is",
        "explain api",
        "explain what an api",
    ]
    if any(phrase in lower for phrase in ordinary_explanations):
        return "ordinary"

    explicit_agent_patterns = [
        r"\bagent\b",
        r"\breact\b",
        r"tool[- ]use",
        r"function[- ]calling",
        r"tool[- ]schema",
        r"\bmcp\b",
        r"browser",
        r"file",
        r"code[- ]execution",
        r"\bapi\b.*\bretriev",
        r"observ",
    ]
    return "agent" if any(re.search(pattern, lower) for pattern in explicit_agent_patterns) else "ordinary"


def test_required_files_exist() -> None:
    for path in [SKILL, ORDINARY, AGENT, CHECKLIST, EXAMPLES, CASES]:
        assert_true(path.exists(), f"Missing required file: {path}")


def test_skill_frontmatter() -> None:
    data = frontmatter(read(SKILL))
    assert_true(data.get("name") == "prompt-engineer", "Skill name must be prompt-engineer")
    description = data.get("description", "")
    assert_true("prompt" in description.lower(), "Description should mention prompts")
    assert_true("function/tool schema" in description, "Description should cover tool schemas")


def test_reference_links_exist() -> None:
    text = read(SKILL)
    for rel in [
        "references/prompt-optimizer-meta-prompt.md",
        "references/agent-prompt-optimizer-meta-prompt.md",
        "references/quality-checklist.md",
        "examples/requests.md",
    ]:
        assert_true(rel in text, f"SKILL.md should reference {rel}")
        assert_true((SKILL_ROOT / rel).exists(), f"Referenced path does not exist: {rel}")


def test_markdown_fences_are_balanced() -> None:
    for path in [ORDINARY, AGENT]:
        fences = fence_lines(read(path))
        assert_true(len(fences) == 2, f"{path.relative_to(SKILL_ROOT)} should have exactly one fenced meta prompt")


def test_default_and_agent_prompts_are_separated() -> None:
    ordinary = read(ORDINARY)
    agent = read(AGENT)

    assert_true("# Tools [optional]" not in ordinary, "Ordinary meta prompt must not include tool schema template")
    assert_true("# Tools [optional]" in agent, "Agent meta prompt should include optional tools section")
    assert_true("Do not add agent, ReAct, tool-use" in ordinary, "Ordinary prompt should guard against accidental agent behavior")
    assert_true("Agent / ReAct behavior" in agent, "Agent prompt should include agent behavior guidance")


def test_agent_route_terms_are_aligned() -> None:
    skill = read(SKILL)
    ordinary = read(ORDINARY)
    agent = read(AGENT)
    for term in AGENT_ROUTE_TERMS:
        assert_true(term in skill, f"Route term missing from SKILL.md: {term}")
        assert_true(term in ordinary, f"Route term missing from ordinary handoff guard: {term}")
        assert_true(term in agent, f"Route term missing from agent prompt: {term}")


def test_commentary_rule_is_scoped_to_completed_prompt_delivery() -> None:
    for path in [ORDINARY, AGENT]:
        text = read(path)
        assert_true(
            "When the requested deliverable is the completed prompt itself" in text,
            f"{path.relative_to(SKILL_ROOT)} must scope no-commentary rule to completed prompt delivery",
        )


def test_readme_installation_boundary() -> None:
    if not README.exists():
        print("SKIP README boundary check outside source repo")
        return
    text = read(README)
    assert_true("skills/prompt-engineer" in text, "README should state the installable skill folder")
    assert_true(
        "${CODEX_HOME:-$HOME/.codex}/skills/prompt-engineer" in text,
        "README should include local install path",
    )


def test_behavior_route_cases() -> None:
    cases = json.loads(read(CASES))
    assert_true(cases, "cases.json should contain route cases")
    for case in cases:
        actual = routed_by_test_oracle(case["request"])
        assert_true(
            actual == case["expected_route"],
            f"{case['name']} expected {case['expected_route']} route but got {actual}",
        )


def main() -> int:
    tests = [
        test_required_files_exist,
        test_skill_frontmatter,
        test_reference_links_exist,
        test_markdown_fences_are_balanced,
        test_default_and_agent_prompts_are_separated,
        test_agent_route_terms_are_aligned,
        test_commentary_rule_is_scoped_to_completed_prompt_delivery,
        test_readme_installation_boundary,
        test_behavior_route_cases,
    ]
    failures: list[str] = []
    for test in tests:
        try:
            test()
            print(f"PASS {test.__name__}")
        except Exception as exc:  # noqa: BLE001 - simple no-dependency test runner.
            failures.append(f"FAIL {test.__name__}: {exc}")
            print(failures[-1])

    print(f"\n{len(tests) - len(failures)} passed, {len(failures)} failed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
