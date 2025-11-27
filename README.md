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

## Usability & Optimization Tools
*   **The Librarian (`get_technique_guide`)**: Returns a guide to available techniques, helping you or the LLM choose the right tool for the job.
*   **The Router (`analyze_task_complexity`)**: Analyzes a task description and recommends the most efficient tool (Low/Medium/High complexity).

## Usage Examples

### 1. Discovery (The Librarian)
```bash
mcp call get_technique_guide --arg category="reasoning"
```

### 2. Auto-Dispatch (The Router)
```bash
mcp call analyze_task_complexity --arg task_description="I need to refactor the auth module and add tests"
```

### 3. Getting a Protocol Shell
```bash
mcp call get_protocol_shell --arg name="reasoning.systematic"
```

### 4. Getting a Molecular Template
```bash
mcp call get_molecular_template
```

## Acknowledgments

Special thanks to:
*   **[Andrej Karpathy](https://x.com/karpathy/status/1937902205765607626)** for his pioneering work and inspiration in the field of AI.
*   **David Kim** for the [Context Engineering](https://github.com/davidkimai/Context-Engineering) framework, which heavily inspired the architecture of this server.
