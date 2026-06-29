# Prompt Engineer

A Codex skill for designing, reviewing, and refining prompts.

Use it to turn rough task descriptions or existing prompts into clearer system prompts, conservative prompt rewrites, prompt-optimizer meta prompts, or explicit agent/tool-use prompt variants.

## Install

After this repository is published to GitHub, install it with the `skills` CLI:

```bash
npx skills add jax-ho/prompt-engineer -g -a codex -y
```

To inspect the available skill before installing:

```bash
npx skills add jax-ho/prompt-engineer --list
```

To try the skill without installing it permanently:

```bash
npx skills use jax-ho/prompt-engineer
```

## Local Development

From a local clone, list the detected skills:

```bash
npx skills add . --list
```

Install the local working tree into Codex:

```bash
npx skills add . -g -a codex -y
```

Manual install also works because the repo root is the installable skill root:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R . "${CODEX_HOME:-$HOME/.codex}/skills/prompt-engineer"
```

## Usage

In Codex, ask naturally:

```text
Improve this prompt conservatively:
Summarize the following meeting notes in a useful way.
```

Or call it explicitly:

```text
$prompt-engineer

Optimize this into an agent prompt:
Create a research assistant that can retrieve internal docs and call a project status API.
```

## Routing

The skill has two source meta prompts:

- `references/prompt-optimizer-meta-prompt.md` is the default for ordinary prompt review, generation, and improvement.
- `references/agent-prompt-optimizer-meta-prompt.md` is used only when the user explicitly asks for agent-style behavior such as agent, ReAct, tool-use, function-calling, tool-schema, MCP, browser/file/code-execution, API, retrieval, or observation-based prompts.

This split keeps ordinary prompt optimization simple while still supporting agent prompts when requested.

## Repository Layout

```text
.
├── SKILL.md
├── references/
│   ├── prompt-optimizer-meta-prompt.md
│   ├── agent-prompt-optimizer-meta-prompt.md
│   └── quality-checklist.md
├── examples/
│   └── requests.md
└── tests/
    ├── cases.json
    └── test_skill_contract.py
```

## Testing

Run the local contract tests:

```bash
python3 tests/test_skill_contract.py
```

The tests verify:

- required files and frontmatter
- reference links
- ordinary vs agent meta prompt separation
- route vocabulary alignment
- README install guidance
- representative ordinary and agent routing cases
