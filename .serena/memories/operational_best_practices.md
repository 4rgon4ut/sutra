# Sutra Project: Operational Best Practices

## Commit Style & Git Workflow

### Commit Message Guidelines
- **Detailed, kernel-style commits**: Use detailed multi-line commit messages
- **Format**: `scope: brief description` followed by detailed explanation
- **Scope prefixes**: 
  - `core:` for core/ module changes
  - `cognitive:` for cognitive/ module changes  
  - `tests:` for test changes
  - `docs:` for documentation
  - `refactor:` for refactoring
  - `fix:` for bug fixes
  - `feat:` for new features

### Examples from Git History:
```
tests: cover thinking models and cell protocols

Added comprehensive test coverage for:
- All four thinking model tools (understand_question, verify_logic, backtracking, symbolic_abstract)
- Windowed and episodic cell protocols
- Fixed template formatting bugs in backtracking and symbolic_abstract
```

```
core: add cell protocol templates

Implemented three memory protocol templates:
- Key-value: Simple state management
- Windowed: Sliding context window with eviction
- Episodic: Write-only log for long-horizon recall
```

### Files to NEVER Commit
- `.journal.md` - Personal journal/notes
- `__pycache__/` directories
- `.venv/` virtual environment
- `.DS_Store` macOS metadata
- `*.pyc` compiled Python files

## Code Organization Principles

### Abstraction Layers (Bottom-Up)
1. **Atoms** (`core/atoms.py`): Basic protocol shell structures
2. **Molecules** (`core/molecules.py`): Composed context templates
3. **Cells** (`core/cells.py`): Memory protocols with state
4. **Programs** (`core/programs.py`): Executable prompt programs
5. **Cognitive Tools** (`cognitive/thinking_models.py`): Advanced reasoning

### Registry Pattern
- All template types use registries (dict mappings)
- Pattern: `{NAME}_REGISTRY = {...}`
- Getter functions: `get_{type}_template()`
- Enables easy extension without modifying core logic

### Template String Formatting
**CRITICAL**: Protocol shell templates use `{}` syntax which conflicts with Python `.format()`

**Rule**: Always escape literal braces in templates by doubling them:
```python
# WRONG - will cause ValueError
template = """
/protocol.name{
    input={key="{value}"}
}
"""

# CORRECT - escaped braces
template = """
/protocol.name{{
    input={{key="{value}"}}
}}
"""
```

**Bug Fix Applied**: Fixed backtracking and symbolic_abstract templates (src/context_engineering_mcp/cognitive/thinking_models.py:138-160, 189-210)

## Testing Practices

### Test Coverage Requirements
- Every MCP tool MUST have a test
- Every template registry MUST have a test
- Test both success and error cases (e.g., unknown template lookup)

### Test Structure (pytest)
```python
def test_feature_name():
    """Clear docstring explaining what's tested."""
    # Arrange
    input_data = ...
    
    # Act
    result = function_under_test(input_data)
    
    # Assert
    assert expected_behavior in result
```

### Current Test Coverage (12 tests, all passing):
1. ✅ Protocol shells (generic and registry-based)
2. ✅ Technique guide
3. ✅ Task complexity analysis
4. ✅ Prompt programs (math and unknown)
5. ✅ Molecular templates
6. ✅ Resources (CoT molecules, reference layers)
7. ✅ Cell protocols (key_value, windowed, episodic, unknown)
8. ✅ All four thinking model tools

### Running Tests
```bash
# Using uv (recommended)
uv run pytest test_server.py -v

# Coverage report
uv run pytest test_server.py --cov=src/context_engineering_mcp
```

## Dependency Management

### Using uv (modern Python package manager)
```bash
# Install dependencies
uv sync

# Add new dependency
uv add package-name

# Add dev dependency
uv add --dev package-name

# Run commands in venv
uv run python script.py
uv run pytest
```

### Dependencies
- **Required**: `mcp` (Model Context Protocol SDK)
- **Dev**: `pytest`, `pytest-cov`
- **Python**: 3.11+ required

## Extension Guidelines

### Adding New Protocol Template (Molecule)
1. Add template constant to `core/molecules.py`
2. Add entry to `PROTOCOL_REGISTRY`
3. Add test to `test_server.py`

### Adding New Cell Protocol
1. Add template constant to `core/cells.py`
2. Add entry to `CELL_PROTOCOL_REGISTRY`
3. Add test to `test_server.py`

### Adding New Thinking Model Tool
1. Add tool function to `cognitive/thinking_models.py`
2. Register with `@mcp.tool()` decorator
3. Export in `__all__`
4. Add test to `test_server.py`

### Adding New MCP Tool (server.py)
1. Define function with appropriate parameters
2. Register with `@mcp.tool()` decorator
3. Add docstring (becomes tool description)
4. Add test

## Vendor-Neutral Naming

**Principle**: Use vendor-neutral, framework-agnostic terminology

**Examples**:
- ✅ "Context Engineering" not "Claude-specific prompting"
- ✅ "Protocol Shell" not "Anthropic template"
- ✅ "Molecular Context" not "GPT-4 few-shot"
- ✅ "Thinking Models" not "Claude reasoning"

**Rationale**: Sutra aims to be a general framework applicable across LLM providers

## Error Handling Patterns

### Graceful Fallbacks
```python
def get_template(name: str) -> str:
    """Retrieve template with fallback."""
    if name in REGISTRY:
        return REGISTRY[name]
    else:
        # Return helpful error message, not crash
        return f"Template '{name}' not found. Available: {list(REGISTRY.keys())}"
```

### Missing Dependencies
- Use dummy harnesses in tests when MCP unavailable
- Example: `test_thinking_models_tools_render()` uses `DummyMCP` class

## Documentation Standards

### Code Documentation
- **Functions**: Clear docstrings with Args/Returns sections
- **Modules**: Module-level docstring explaining purpose
- **Templates**: Inline comments for complex protocol shells

### External Documentation
- `.context/` directory: Comprehensive guides and examples
- `README.md`: Quick start and overview
- `QUICKSTART.md`: Step-by-step tutorial

## Performance Considerations

### Serena Memory Usage
- Store architectural knowledge, not ephemeral data
- Memory files are persistent across sessions
- Keep memories focused and well-organized

### Template Caching
- Templates are constants (loaded once at import)
- No need for runtime caching

## Security Practices

### Input Validation
- Validate template names against registries
- Sanitize user inputs in protocol shells
- No arbitrary code execution

### Secrets Management
- Never commit API keys or tokens
- Use environment variables for sensitive config
- `.env` files in `.gitignore`

## Maintenance Checklist

### Before Committing
- [ ] Run tests: `uv run pytest`
- [ ] Format code: `uv run ruff format`
- [ ] Lint: `uv run ruff check`
- [ ] Update tests if adding features
- [ ] Write detailed commit message
- [ ] Verify `.journal.md` not staged

### Before Releasing
- [ ] All tests passing
- [ ] Documentation updated
- [ ] Examples working
- [ ] Version bumped in `pyproject.toml`

## Common Gotchas

1. **Template Formatting**: Remember to escape `{}` braces
2. **Test Isolation**: Use DummyMCP to avoid MCP import issues
3. **Registry Keys**: Use consistent naming (e.g., `cell.protocol.*`)
4. **Optional Parameters**: Provide defaults or normalize to `"<none>"`

## Project Philosophy

**Context Engineering Framework**
- Systematic approach to prompt construction
- Layered abstraction (atoms → molecules → cells → programs)
- Protocol shells for structure and reproducibility
- Vendor-neutral and framework-agnostic
- Evidence-based practices from research

**Quality Over Speed**
- Comprehensive tests before merging
- Detailed commits for maintainability
- Clear documentation for users
- Thoughtful abstractions, not hasty implementations
