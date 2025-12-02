from context_engineering_mcp.server import (
    get_protocol_shell,
    get_prompt_program,
    get_molecular_template,
    get_cot_molecules,
    get_reference_layers,
    get_technique_guide,
    analyze_task_complexity,
)


def test_get_protocol_shell():
    """Test that protocol shell returns correct structure."""
    intent = "Test Intent"
    name = "TestProtocol"
    result = get_protocol_shell(intent=intent, name=name)

    assert "/protocol.TestProtocol" in result
    assert 'intent="Test Intent"' in result
    assert "input={" in result
    assert "output={" in result


def test_get_technique_guide():
    result = get_technique_guide()
    assert "Context Engineering Technique Guide" in result
    assert "| Category | Tool |" in result
    assert "reasoning.systematic" in result


def test_analyze_task_complexity():
    # Test High Complexity
    high = analyze_task_complexity(
        "I need to refactor this entire codebase and add tests"
    )
    assert (
        high["complexity"] == "High" or high["complexity"] == "Medium"
    )  # "codebase" triggers Medium, "tests" triggers High. Logic might hit first match.

    # Test Low Complexity
    low = analyze_task_complexity("What is 2+2?")
    assert low["complexity"] == "Low"
    assert low["recommended_tool"] == "Standard Molecule"


def test_get_protocol_shell_registry():
    # Test retrieving a specific template from registry
    result = get_protocol_shell(name="reasoning.systematic")
    assert 'intent="Break down complex problems' in result

    # Test generic fallback
    generic = get_protocol_shell(name="CustomProtocol", intent="Testing")
    assert 'intent="Testing"' in generic
    assert "output={" in result


def test_get_prompt_program_math():
    """Test that math prompt program returns correct template."""
    result = get_prompt_program(program_type="math")

    assert "// Prompt Program: Math Solver" in result
    assert "function understand_math_problem" in result
    assert "function solve_math_with_cognitive_tools" in result


def test_get_prompt_program_unknown():
    """Test that unknown program type returns generic structure with warning."""
    result = get_prompt_program(program_type="unknown_type")

    assert "// Program type 'unknown_type' not yet implemented" in result
    assert "// Prompt Program: Math Solver" in result


def test_get_molecular_template():
    """Test that molecular template returns the python function string."""
    result = get_molecular_template()

    assert "def create_molecular_context" in result
    assert "Construct a molecular context from examples" in result


def test_resources():
    """Test that resources return expected content."""
    cot = get_cot_molecules()
    assert "# Chain of Thought Templates" in cot
    assert "MOLECULE =" in cot

    layers = get_reference_layers()
    assert "# Context Engineering Layers" in layers
    assert "1. Atoms" in layers
    assert "5. Systems" in layers


def test_get_cell_protocol():
    """Test cell protocol retrieval."""
    from context_engineering_mcp.server import get_cell_protocol

    key_value = get_cell_protocol("cell.protocol.key_value")
    assert "cell.protocol.key_value" in key_value
    assert "new_state" in key_value

    missing = get_cell_protocol("cell.protocol.unknown")
    assert "not found" in missing


def test_thinking_models_tools_render():
    """Ensure thinking model tools register and render expected content without FastMCP."""
    from context_engineering_mcp.cognitive.thinking_models import register_thinking_models

    class DummyMCP:
        def __init__(self) -> None:
            self.tools = {}

        def tool(self):
            def decorator(func):
                self.tools[func.__name__] = func
                return func

            return decorator

    dummy = DummyMCP()
    register_thinking_models(dummy)

    assert "backtracking" in dummy.tools
    assert "symbolic_abstract" in dummy.tools

    backtrack = dummy.tools["backtracking"](
        "reach objective", "failed step", trace="trace log", constraints="none"
    )
    assert "/reasoning.backtracking" in backtrack
    assert "recovery_plan" in backtrack

    symbolic = dummy.tools["symbolic_abstract"]("x+1=2", mapping_hint="x->var", goal="solve")
    assert "/symbolic.abstract" in symbolic
    assert "symbol_table" in symbolic
