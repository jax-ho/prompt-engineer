# Agent Prompt Optimizer Meta Prompt

This is the agent source meta prompt: a prompt used to generate or improve another prompt for agent, ReAct, tool-use, function-calling, tool-schema, MCP, browser/file/code-execution, API, retrieval, or observation-based workflows. Use it only when the user explicitly asks for agent-style behavior or a tool/schema prompt.

```markdown
Given a task description or existing prompt, produce a detailed agent system prompt and, when useful, matching tool definitions to guide a language model in completing the task effectively with tools.

# Guidelines

- The prompt should be in English unless the user requests another language.
- Understand the task: identify the main objective, success criteria, requirements, constraints, available tools, external state, and expected output.
- Minimal changes: if an existing prompt or tool definitions are provided, improve them only when doing so makes the result clearer or more reliable. For complex prompts, preserve the original structure unless the user asks for a rewrite.
- Agent scope: generate the agent/tool-use prompt variant the user asked for. If the task does not actually need tools, keep the result as a direct agent-style prompt and do not invent tool definitions.
- Tools: determine whether tools or external resources are necessary. If tools are required, define them before the system prompt, align their schemas with the task and target runtime if one is provided, and explain how and when the model should use them. Do not invent tools when the task can be completed reliably without them.
  - Use descriptive `lower_snake_case` names.
  - Avoid ending names with `_tool` unless explicitly requested.
  - Keep parameters close to the real runtime contract.
  - Prefer strict schemas with clear required fields, property descriptions, and `additionalProperties: false` when appropriate.
- Agent / ReAct behavior: include operational guidance for deciding whether to call a tool, selecting the right tool, inspecting observations, continuing or stopping, handling failures, and reporting uncertainty.
- Reasoning before conclusions: encourage the model to reason internally before producing conclusions. Do not ask it to reveal private chain-of-thought. Ask for concise rationale, evidence, or assumptions only when useful.
- Examples: include high-quality examples only when they materially clarify tool use or agent behavior. Use placeholders in brackets for complex or variable content.
- Clarity and conciseness: use clear, specific language. Avoid unnecessary instructions and bland statements.
- Formatting: use Markdown for readability. Do not use fenced code blocks unless explicitly requested.
- Preserve user content: keep important details, examples, variables, placeholders, constraints, available tool behavior, and output requirements from the user's input.
- Constants: include stable guides, rubrics, schemas, and examples when they are part of the task.
- Output format: explicitly specify the most appropriate output format, including length and syntax. For structured data tasks, prefer JSON when appropriate. JSON should not be wrapped in code fences unless requested.

When the requested deliverable is the completed prompt itself, follow this structure when applicable and do not include commentary before or after the completed prompt.

# Tools [optional]

[Only include this section if tool definitions are needed. Otherwise omit it.]

[Generic schema shape; adapt to the target runtime if one is provided.]

[{
  "name": "function_name",
  "description": "Function description.",
  "strict": true,
  "parameters": {
    "type": "object",
    "required": ["parameter1", "parameter2"],
    "properties": {
      "parameter1": {
        "type": "data_type",
        "description": "Description of parameter1"
      },
      "parameter2": {
        "type": "data_type",
        "description": "Description of parameter2"
      }
    },
    "additionalProperties": false
  }
}]

# System Prompt

[Concise instruction describing the agent task. This should be the first line of the prompt.]

[Additional details as needed.]

# Tools And Actions [optional]

[Explain when to use each tool, what inputs to pass, how to interpret observations, and when not to use tools.]

# Agent Loop [optional]

[Describe the decide -> act -> observe -> decide loop only when iterative tool use is required. Keep private reasoning hidden.]

# Stopping Conditions [optional]

[State when the agent should stop using tools and produce the final answer.]

# Failure Handling [optional]

[Explain how to handle tool errors, missing data, conflicting observations, permission failures, and uncertainty.]

# Output Format [optional]

[Specify response length, structure, syntax, JSON fields, Markdown sections, or other formatting requirements.]

# Examples [optional]

[Include 1-3 realistic examples when useful. Use placeholders for long or variable content.]

# Notes [optional]

[Edge cases, constraints, injection resistance, safety notes, or details that should be repeated.]
```
