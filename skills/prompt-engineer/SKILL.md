---
name: prompt-engineer
description: Use when the user asks to design, critique, improve, or generate a prompt, system prompt, meta prompt, prompt optimizer prompt, prompt template, tool-use prompt, ReAct agent prompt, or function/tool schema from a task description or existing prompt.
---

# Prompt Engineer

Use the bundled meta prompts to review, generate, or improve prompts.

## Core Rule

Default to `references/prompt-optimizer-meta-prompt.md` for ordinary prompt review, generation, and improvement.

Use `references/agent-prompt-optimizer-meta-prompt.md` only when the user explicitly asks for an agent-style prompt: agent, ReAct, tool-use, function-calling, tool-schema, MCP, browser/file/code-execution, API, retrieval, or observation-based behavior.

Do not duplicate the meta prompts' full logic in this skill file. This skill routes the task; the reference meta prompt performs the prompt optimization.

## Use For

- Reviewing or critiquing an existing prompt.
- Improving an existing prompt conservatively.
- Generating a system prompt from a task description.
- Creating or improving a meta prompt.
- Creating agent/tool-use/ReAct prompt variants when explicitly requested.

## Minimal Workflow

1. Choose the source meta prompt:
   - Default: read `references/prompt-optimizer-meta-prompt.md`.
   - Agent version: read `references/agent-prompt-optimizer-meta-prompt.md` when the user asks for agent-style behavior: agent, ReAct, tool-use, function-calling, tool-schema, MCP, browser/file/code-execution, API, retrieval, or observation-based behavior.
2. Apply the selected meta prompt to the user's task or existing prompt.
3. Preserve the user's intent, constraints, examples, variables, and important wording.
4. Ask only for blocking missing information.
5. For complex prompt rewrites, tool schemas, or agent prompts, also read `references/quality-checklist.md` before finalizing.
6. Use `examples/requests.md` only when you need response-shape calibration.

## Output

- For critique: give findings first, then minimal suggested edits.
- For rewrite: output only the finished prompt when the user asks for the prompt alone; otherwise a short change note may follow.
- For tools plus prompt: output `# Tools` first only when tool definitions are needed, then `# System Prompt`.
- For discussion: explain the naming, scope, or tradeoff directly without forcing a rewrite.

## References

- `references/prompt-optimizer-meta-prompt.md` for the default ordinary prompt optimizer.
- `references/agent-prompt-optimizer-meta-prompt.md` for agent, ReAct, tool-use, and function/tool-schema prompts.
- `references/quality-checklist.md` before finalizing complex prompt rewrites.
- `examples/requests.md` for typical user request patterns and expected response shapes.
