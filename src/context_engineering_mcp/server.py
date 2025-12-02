from mcp.server.fastmcp import FastMCP

from context_engineering_mcp.cognitive import register_thinking_models
from context_engineering_mcp.core import (
    MOLECULAR_CONTEXT_FUNC,
    format_protocol_shell,
    get_program_template,
    get_protocol_template,
)

# Initialize FastMCP server
mcp = FastMCP("Context Engineering MCP")

# Register cognitive tools
register_thinking_models(mcp)

# --- Tools ---


@mcp.tool()
def get_technique_guide(category: str = "all") -> str:
    """
    Returns a guide to available Context Engineering techniques (The Librarian).
    Use this to discover the best tool for a given task.

    Args:
        category: Filter by 'reasoning', 'workflow', 'code', 'project', or 'all'.
    """
    guide = """
    # Context Engineering Technique Guide

    | Category | Tool | Complexity | Best For |
    |----------|------|------------|----------|
    | **Reasoning** | `reasoning.systematic` | High | Complex problems requiring step-by-step logic. |
    | **Reasoning** | `thinking.extended` | Very High | Deep exploration, trade-off analysis, simulation. |
    | **Workflow** | `workflow.test_driven` | High | Implementing features with TDD. |
    | **Code** | `code.analyze` | Medium | Understanding code structure and quality. |
    | **Project** | `project.explore` | Medium | Mapping a new codebase. |
    | **Basic** | `Standard Molecule` | Low | Simple pattern matching (use `get_molecular_template`). |

    **Usage:**
    Call `get_protocol_shell(name="<Tool Name>")` to retrieve the specific template.
    """
    return guide


@mcp.tool()
def analyze_task_complexity(task_description: str) -> dict:
    """
    Analyzes a task to recommend the most efficient tool (The Router).

    Args:
        task_description: The user's prompt or task.
    """
    task = task_description.lower()

    # Heuristic Analysis
    if any(w in task for w in ["project", "repo", "codebase", "architecture"]):
        return {
            "complexity": "Medium",
            "recommended_tool": "project.explore",
            "reasoning": "Task involves project-level understanding.",
        }
    elif any(w in task for w in ["test", "tdd", "verify"]):
        return {
            "complexity": "High",
            "recommended_tool": "workflow.test_driven",
            "reasoning": "Task involves testing or verification workflows.",
        }
    elif any(w in task for w in ["analyze", "reason", "think", "solve", "complex"]):
        return {
            "complexity": "High",
            "recommended_tool": "reasoning.systematic",
            "reasoning": "Task requires structured reasoning.",
        }
    else:
        return {
            "complexity": "Low",
            "recommended_tool": "Standard Molecule",
            "reasoning": "Task appears simple. Use a basic prompt or few-shot molecule.",
        }


@mcp.tool()
def get_protocol_shell(name: str = "MyProtocol", intent: str | None = None) -> str:
    """
    Returns a Protocol Shell. Can return a specific pre-defined template or a blank shell.

    Args:
        name: The name of the protocol (e.g., 'reasoning.systematic') OR a custom name.
        intent: (Optional) The intent if creating a custom shell.
    """
    template = get_protocol_template(name)
    if template:
        return template

    intent_str = intent or "Define your intent here"
    return format_protocol_shell(name=name, intent=intent_str)


@mcp.tool()
def get_molecular_template() -> str:
    """
    Returns the Python function for creating molecular contexts (Module 02).
    Use this to programmatically construct few-shot prompts.
    """
    return MOLECULAR_CONTEXT_FUNC


@mcp.tool()
def get_prompt_program(program_type: str = "math") -> str:
    """
    Returns a functional pseudo-code prompt template (Module 07).

    Args:
        program_type: The type of program (currently supports 'math').
    """
    return get_program_template(program_type)


# --- Resources ---


@mcp.resource("context://molecules/cot")
def get_cot_molecules() -> str:
    """
    Returns Chain-of-Thought templates (Module 02).
    """
    return """
    # Chain of Thought Templates (Module 02)

    ## Standard CoT
    Q: [Question]
    A: Let's think step by step.
    1. [Step 1]
    2. [Step 2]
    Therefore, the answer is [Answer].

    ## Molecular Context Structure
    MOLECULE = [INSTRUCTION] + [EXAMPLES] + [CONTEXT] + [NEW INPUT]
    """


@mcp.resource("context://reference/layers")
def get_reference_layers() -> str:
    """
    Returns the Context Engineering Layer definitions.
    """
    return """
    # Context Engineering Layers

    1. Atoms: Basic units of meaning (Single Prompts).
    2. Molecules: Combinations of atoms (Few-Shot Templates).
    3. Cells: Functional units (Prompt Programs).
    4. Organs: Specialized structures (Protocol Shells).
    5. Systems: Interconnected networks (Agents).
    """


@mcp.resource("context://fields/resonance")
def get_neural_fields() -> str:
    """
    Returns Neural Field primitives (Module 08-10).
    """
    return """
    # Neural Field Protocols (Module 08-10)

    ## Resonance Field
    A structure for maintaining context persistence across long interaction horizons.

    [FIELD_DEFINITION]
    Type: Resonance
    Decay_Rate: Low
    Attractors: [Core Intent, User Preferences]
    """


def main():
    mcp.run()


if __name__ == "__main__":
    main()
