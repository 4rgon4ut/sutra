import pytest
import json
from context_engineering_mcp.server import get_protocol_shell, get_prompt_program, get_molecular_template, get_cot_molecules, get_reference_layers

def test_get_protocol_shell():
    """Test that protocol shell returns correct structure."""
    intent = "Test Intent"
    name = "TestProtocol"
    result = get_protocol_shell(intent=intent, name=name)

    assert "/protocol.TestProtocol" in result
    assert 'intent="Test Intent"' in result
    assert "input={" in result
    assert "process=[" in result
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
