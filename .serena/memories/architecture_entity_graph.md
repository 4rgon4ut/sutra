# Sutra MCP Server: Architecture & Entity-Relationship Graph

## Overview
Sutra is a Context Engineering MCP server providing systematic tools for prompt construction, cognitive reasoning, and memory management through the Model Context Protocol.

## Directory Structure

```
sutra/
├── src/context_engineering_mcp/
│   ├── core/              # Core abstractions
│   │   ├── atoms.py       # Protocol shells (basic building blocks)
│   │   ├── molecules.py   # Context templates (composed abstractions)
│   │   ├── cells.py       # Memory protocols (stateful patterns)
│   │   └── programs.py    # Prompt programs (executable templates)
│   ├── cognitive/         # Cognitive reasoning tools
│   │   └── thinking_models.py
│   ├── systems/           # System components
│   ├── server.py          # MCP server & tool registration
│   └── templates.py       # Template management
├── test_server.py         # Test suite
└── .context/              # Documentation & examples
    ├── 00_foundations/    # Core concepts
    ├── 10_guides_zero_to_hero/
    ├── 20_templates/
    ├── 30_examples/
    └── 00_COURSE/         # Course materials
```

## Entity Graph

### 1. Core Abstractions (src/context_engineering_mcp/core/)

#### Atoms (atoms.py)
**Purpose**: Basic building blocks - Protocol Shell structures
**Entities**:
- `PROTOCOL_SHELL_STRUCTURE`: Template for protocol shells
- `format_protocol_shell()`: Formatter function

**Exports**: Protocol shell infrastructure

#### Molecules (molecules.py)
**Purpose**: Composed context templates for various reasoning patterns
**Entities**:
- `MOLECULAR_CONTEXT_FUNC`: Functional context template
- `REASONING_SYSTEMATIC`: Systematic reasoning template
- `THINKING_EXTENDED`: Extended thinking template
- `WORKFLOW_TDD`: Test-driven development workflow
- `CODE_ANALYZE`: Code analysis template
- `PROJECT_EXPLORE`: Project exploration template
- `PROTOCOL_REGISTRY`: Registry of all protocol templates
- `get_protocol_template()`: Template retriever

**Exports**: Protocol templates and registry

#### Cells (cells.py)
**Purpose**: Memory protocols for stateful behavior
**Entities**:
- `CELL_PROTOCOL_KEY_VALUE`: Key-value memory protocol
- `CELL_PROTOCOL_WINDOWED`: Windowed memory protocol
- `CELL_PROTOCOL_EPISODIC`: Episodic memory protocol
- `CELL_PROTOCOL_REGISTRY`: Registry of cell protocols
- `get_cell_protocol_template()`: Cell protocol retriever

**Exports**: Memory protocol templates and registry

#### Programs (programs.py)
**Purpose**: Executable prompt programs
**Entities**:
- `PROMPT_PROGRAM_MATH_TEMPLATE`: Mathematical reasoning program
- `get_program_template()`: Program template retriever

**Exports**: Prompt program templates

### 2. Cognitive Tools (src/context_engineering_mcp/cognitive/)

#### Thinking Models (thinking_models.py)
**Purpose**: Advanced reasoning and verification tools
**Entities**:
- `register_thinking_models()`: Registers cognitive tools with MCP

**Registered MCP Tools**:
- `understand_question`: Decompose and clarify user questions
- `verify_logic`: Verify reasoning traces and claims
- `backtracking`: Error correction with recursive backtracking
- `symbolic_abstract`: Convert expressions to abstract symbols

**Exports**: Thinking model registration

### 3. MCP Server (src/context_engineering_mcp/server.py)

**Purpose**: Main MCP server exposing all tools
**MCP Tools Registered**:

1. **Meta Tools** (The Librarian & Router):
   - `get_technique_guide()`: Guide to available techniques
   - `analyze_task_complexity()`: Recommends best tool for task

2. **Protocol Shells** (Module 01):
   - `get_protocol_shell()`: Returns protocol shell templates

3. **Molecular Templates** (Module 02):
   - `get_molecular_template()`: Returns molecular context function

4. **Prompt Programs** (Module 07):
   - `get_prompt_program()`: Returns functional pseudo-code templates

5. **Cell Protocols** (Module 03):
   - `get_cell_protocol()`: Returns memory behavior templates

6. **Additional Retrieval Tools**:
   - `get_cot_molecules()`: Chain-of-thought molecules
   - `get_reference_layers()`: Reference materials
   - `get_neural_fields()`: Neural field contexts

**Entry Point**:
- `main()`: Starts MCP server with all tools

### 4. Templates (src/context_engineering_mcp/templates.py)

**Purpose**: Template management and rendering
**Role**: Central registry and loader for all template types

### 5. Tests (test_server.py)

**Test Coverage**:
- ✅ `test_get_protocol_shell()`: Protocol shell rendering
- ✅ `test_get_technique_guide()`: Technique guide tool
- ✅ `test_analyze_task_complexity()`: Task analysis tool
- ✅ `test_get_protocol_shell_registry()`: Registry-based shell retrieval
- ✅ `test_get_prompt_program_math()`: Math program template
- ✅ `test_get_prompt_program_unknown()`: Unknown program fallback
- ✅ `test_get_molecular_template()`: Molecular template rendering
- ✅ `test_resources()`: MCP resources listing
- ✅ `test_get_cell_protocol()`: Cell protocol template rendering
- ✅ `test_thinking_models_tools_render()`: Thinking model tool rendering

## Relationship Graph

```
server.py
    ├──[imports]──> core/__init__.py
    │                  ├──[exports]──> atoms.py
    │                  ├──[exports]──> molecules.py
    │                  ├──[exports]──> cells.py
    │                  └──[exports]──> programs.py
    ├──[imports]──> cognitive/__init__.py
    │                  └──[exports]──> thinking_models.py
    ├──[imports]──> templates.py
    └──[registers]──> MCP Tools:
                          - get_technique_guide
                          - analyze_task_complexity
                          - get_protocol_shell
                          - get_molecular_template
                          - get_prompt_program
                          - get_cell_protocol
                          - get_cot_molecules
                          - get_reference_layers
                          - get_neural_fields
                          - understand_question
                          - verify_logic
                          - backtracking
                          - symbolic_abstract

test_server.py
    └──[tests]──> All MCP tools
```

## Abstraction Layers

### Layer 0: Atoms
- **Concept**: Minimal prompt structures (protocol shells)
- **Example**: `/protocol.shell{intent, input, process, output}`
- **Module**: `atoms.py`

### Layer 1: Molecules  
- **Concept**: Composed context templates (few-shot, CoT)
- **Examples**: REASONING_SYSTEMATIC, WORKFLOW_TDD
- **Module**: `molecules.py`

### Layer 2: Cells
- **Concept**: Memory protocols (stateful behavior)
- **Examples**: Key-Value, Windowed, Episodic
- **Module**: `cells.py`

### Layer 3: Organs/Programs
- **Concept**: Executable prompt programs
- **Examples**: Math solver, Debate facilitator
- **Module**: `programs.py`

### Layer 4: Cognitive Tools
- **Concept**: Advanced reasoning & verification
- **Examples**: Backtracking, Symbolic abstraction
- **Module**: `thinking_models.py`

## Key Patterns & Conventions

1. **Registry Pattern**: All template types use registries (PROTOCOL_REGISTRY, CELL_PROTOCOL_REGISTRY)
2. **Getter Functions**: Each module provides `get_*_template()` functions
3. **MCP Tool Naming**: Tools use descriptive names (get_protocol_shell, understand_question)
4. **Template Structure**: Templates are string constants with placeholders
5. **Modular Organization**: Clear separation between atoms → molecules → cells → programs
6. **Test Coverage**: Each MCP tool has corresponding test

## Extension Points

To add new functionality:

1. **New Protocol Template** → Add to `molecules.py` PROTOCOL_REGISTRY
2. **New Cell Protocol** → Add to `cells.py` CELL_PROTOCOL_REGISTRY  
3. **New Program** → Add to `programs.py`
4. **New Thinking Tool** → Register in `thinking_models.py`
5. **New MCP Tool** → Register in `server.py` main()

## Dependencies

- **MCP SDK**: `@anthropic-ai/sdk` for MCP protocol
- **Python**: Python 3.11+ required
- **Testing**: pytest for test execution
