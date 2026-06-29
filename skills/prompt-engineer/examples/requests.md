# Example Request Patterns

## Critique An Existing Prompt

User asks:

> Read this prompt and tell me whether it needs optimization.

Response shape:

1. State the prompt's current purpose.
2. List the highest-risk issues first.
3. Distinguish must-fix problems from optional polish.
4. Suggest minimal edits rather than a full rewrite unless needed.

## Rewrite A Prompt Conservatively

User asks:

> Improve this prompt, but do not make it worse.

Response shape:

1. Preserve the original structure where possible.
2. Patch unclear or risky lines.
3. Avoid extra sections unless they fix a real behavior gap.
4. Summarize what changed and why.

## Generate A Tool-Use Prompt

User asks:

> Turn this task into a system prompt with tools.

Response shape:

1. Define tools only if they are actually needed.
2. Put `# Tools` before `# System Prompt`.
3. Include tool selection and stopping rules.
4. Keep tool parameters close to the runtime contract.

## Generate A ReAct Agent Prompt

User asks:

> Make this a ReAct prompt.

Response shape:

1. Confirm the task needs iterative tool-use or observations.
2. Include rules for deciding whether to call a tool.
3. Include rules for reading observations and continuing or stopping.
4. Include failure and uncertainty handling.
5. Do not require visible chain-of-thought.
