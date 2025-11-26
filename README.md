# sutra

A Model Context Protocol (MCP) server providing structured prompting templates, protocol shells, and neural field architectures for advanced LLM reasoning.

## Core Capabilities

*   **Molecules**: Templates for few-shot learning and Chain-of-Thought (CoT) patterns.
*   **Protocols**: Structured reasoning shells defined by Intent, Input, Process, and Output.
*   **Fields**: Primitives for neural field context persistence and resonance.

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

## Usage Example

Retrieve a **Protocol Shell** to structure a new cognitive tool:

```python
# Using an MCP client
result = await client.call_tool(
    "get_protocol_shell",
    arguments={
        "intent": "Analyze user sentiment",
        "name": "SentimentAnalyzer"
    }
)
print(result.content[0].text)
```

Retrieve a **Molecular Context** template:

```python
# Get the Python function for constructing molecules
template_code = await client.call_tool("get_molecular_template")
```
