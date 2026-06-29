# Quality Checklist

Use this before finalizing prompt rewrites, tool-use prompts, or meta prompts.

## Fit

- The prompt directly supports the user's actual task.
- The prompt does not add unrequested scope, roles, style, or tooling.
- The prompt is only as long as needed for reliable behavior.
- The prompt keeps important user-provided constraints and examples.

## Structure

- The first instruction is clear and actionable.
- Process guidance appears before output requirements.
- Output format is explicit and testable.
- Optional sections are omitted when they do not add control.
- Examples are realistic enough to teach the behavior, or omitted.

## Reasoning

- The prompt tells the model to reason internally where useful.
- The prompt does not require revealing private chain-of-thought.
- If rationale is needed, it asks for concise evidence, assumptions, or explanation.
- Conclusions, classifications, and final answers appear after supporting evidence when the output includes both.

## Tools

- Tool definitions are included only when the task materially needs them.
- Tool names are descriptive `lower_snake_case`.
- Schemas are strict enough for the runtime: required fields, property descriptions, and `additionalProperties: false` when appropriate.
- Tool-use instructions say when to call tools, how to handle results, and when to stop.
- No tool capability is invented beyond the available runtime.

## ReAct / Agentic Work

- ReAct guidance is included only for iterative observation-based work.
- The prompt includes tool selection, observation handling, stopping conditions, and failure handling.
- The prompt does not merely say "follow ReAct" without operational rules.
- The final response requirements are separate from the private reasoning loop.

## Final Safety Pass

- No unsupported facts, citations, product details, or examples were invented.
- Ambiguity is handled by assumptions or narrow clarifying questions.
- The result is easy to copy into the intended system prompt or skill.
