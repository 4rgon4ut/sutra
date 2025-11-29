# sutra

A Model Context Protocol (MCP) server providing structured prompting templates, protocol shells, and neural field architectures for advanced LLM reasoning.

## Core Capabilities

*   **Molecules**: Templates for few-shot learning and Chain-of-Thought (CoT) patterns.
*   **Protocols**: Structured reasoning shells defined by Intent, Input, Process, and Output.
*   **Fields**: Primitives for neural field context persistence and resonance.

## TODO / WIP

**Done**
- MCP server exposing template registry for molecules, protocols, and neural field primitives.
- Librarian (`get_technique_guide`) and Router (`analyze_task_complexity`) for tool discovery and selection.
- Protocol shell retrieval for reasoning, workflow, project, and code analysis templates.
- Molecular context builder plus math prompt program utility.
- Context resources: CoT molecules, layer reference, and resonance field primitives.

**Upcoming**
- [ ] Context sqeezing/pruning/sumarization
- [ ] Interactive context build-up
- [ ] Semantic Chunking
- [ ] Check interaction and not to overlap existing popular tools functionality (like memory mcp, sequential thinking)
- [ ] HALLUCINATION REDUCTION STRATEGIES
- [ ] Token/Quality rate
- [ ] Layered memory organization in interactive context building
- [ ] create preconfigured roles templates like orchestrator --> shared_context manager --> specialist_1, specialist_2, ...
- [ ] One of the most powerful organ patterns is ReAct (Reasoning + Acting): thought --> action --> observation; continue loop

## Installation & Configuration

### Installation

We recommend using `uv` for a fast and reliable installation:

```bash
uv tool install .
```

Or using `pip`:

```bash
pip install .
```

### Updating

To update to the latest version of your local copy:

```bash
uv tool install . --force
```
or
```bash
pip install . --upgrade
```

### Configuration

#### Claude Desktop
Add to `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "sutra": {
      "command": "uv",
      "args": ["run", "context-engineering-mcp"]
    }
  }
}
```

#### Gemini CLI
Add to `~/.gemini/settings.json`:
```json
{
  "mcpServers": {
    "sutra": {
      "command": "uv",
      "args": ["run", "context-engineering-mcp"]
    }
  }
}
```

#### Continue.dev (VS Code / JetBrains)
Add to `~/.continue/config.json`:
```json
{
  "mcpServers": [
    {
      "name": "sutra",
      "command": "uv",
      "args": ["run", "context-engineering-mcp"]
    }
  ]
}
```

#### Codex
Add to your configuration file (TOML):
```toml
[mcp_servers.sutra]
command = "uv"
args = ["run", "context-engineering-mcp"]
```

## Usability & Optimization Tools
*   **The Librarian (`get_technique_guide`)**: Returns a guide to available techniques, helping you or the LLM choose the right tool for the job.
*   **The Router (`analyze_task_complexity`)**: Analyzes a task description and recommends the most efficient tool (Low/Medium/High complexity).

## Programmatic Usage (Python)

You can use the `mcp` library to connect to the server programmatically:

```python
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    # 1. Connect to the server
    server = StdioServerParameters(command="uv", args=["run", "context-engineering-mcp"])

    async with stdio_client(server) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # 2. Call a tool (Simple & Direct)
            result = await session.call_tool("get_technique_guide", arguments={})
            print(result.content[0].text)

            # 3. Get a specific template
            shell = await session.call_tool("get_protocol_shell", arguments={"name": "code.analyze"})
            print(shell.content[0].text)

```

## Troubleshooting

### "The model doesn't see my tools"
If you are using **Continue** or a similar extension and the model says it can't find the tools:
1.  **Restart VS Code**: MCP servers often need a restart to register.
2.  **Check the Logs**: Look at the "Output" tab in VS Code and select "Continue" (or your extension) to see if the server crashed.
3.  **Be Explicit**: Sometimes the model needs a nudge. Try asking:
    > "Please call the `get_technique_guide` tool."
4.  **Check Model Support**: Ensure you are using a model that supports tool calling (e.g., Gemini 1.5 Pro, Claude 3.5 Sonnet).

### "Gemini Code Assist" (Official Extension)
Note: The official Google Gemini Code Assist extension may have different MCP support than community extensions like Continue. Check the official documentation for how to enable MCP servers.

## CLI Usage (via MCP CLI)

If you have the `mcp-cli` installed, you can call tools directly:

```bash
mcp call get_technique_guide --arg category="reasoning"
```

## Acknowledgments

Special thanks to:
*   **[Andrej Karpathy](https://x.com/karpathy/status/1937902205765607626)** for his pioneering work and inspiration in the field of AI.
*   **David Kim** for the [Context Engineering](https://github.com/davidkimai/Context-Engineering) framework, which heavily inspired the architecture of this server.
