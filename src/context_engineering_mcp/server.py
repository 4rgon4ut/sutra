from mcp.server.fastmcp import FastMCP
from typing import Dict, Any

# Initialize FastMCP server
mcp = FastMCP("Context Engineering MCP")

# --- Constants & Templates ---

PROTOCOL_SHELL_STRUCTURE = """
/protocol.{name}{{
    intent="{intent}",
    input={{
        param1="value1",
        param2="value2"
    }},
    process=[
        /step1{{action="do something"}},
        /step2{{action="do something else"}}
    ],
    output={{
        result1="expected output 1",
        result2="expected output 2"
    }}
}}
"""

MOLECULAR_CONTEXT_FUNC = """
def create_molecular_context(instruction, examples, new_input, format_type="input-output"):
    \"\"\"
    Construct a molecular context from examples (Module 02).

    Args:
        instruction (str): The task instruction
        examples (List[Dict]): List of example input/output pairs
        new_input (str): The new input to process
        format_type (str): Template type (input-output, chain-of-thought)

    Returns:
        str: The complete molecular context
    \"\"\"
    context = f"{instruction}\\n\\n"

    # Add examples based on format type
    if format_type == "input-output":
        for example in examples:
            context += f"Input: {example['input']}\\n"
            context += f"Output: {example['output']}\\n\\n"
    elif format_type == "chain-of-thought":
        for example in examples:
            context += f"Input: {example['input']}\\n"
            context += f"Thinking: {example['thinking']}\\n"
            context += f"Output: {example['output']}\\n\\n"

    # Add the new input
    context += f"Input: {new_input}\\nOutput:"

    return context
"""

PROMPT_PROGRAM_MATH_TEMPLATE = """
// Prompt Program: Math Solver (Module 07)

function understand_math_problem(problem) {
  return `
    Task: Analyze this math problem thoroughly before solving.
    Problem: ${problem}
    Please provide:
    1. What type of math problem is this?
    2. What are the key variables or unknowns?
    3. What are the given values or constraints?
    4. What formulas or methods will be relevant?
  `;
}

function plan_solution_steps(problem_analysis) {
  return `
    Task: Create a step-by-step plan to solve this math problem.
    Problem Analysis: ${problem_analysis}
    Please outline a specific sequence of steps to solve this problem.
  `;
}

function execute_solution(problem, solution_plan) {
  return `
    Task: Solve this math problem following the provided plan.
    Problem: ${problem}
    Solution Plan: ${solution_plan}
    Please show all work for each step.
  `;
}

function verify_solution(problem, solution) {
  return `
    Task: Verify the correctness of this math solution.
    Original Problem: ${problem}
    Proposed Solution: ${solution}
    Please check calculations and logic.
  `;
}

// Main problem-solving function
function solve_math_with_cognitive_tools(problem) {
  problem_analysis = LLM(understand_math_problem(problem));
  solution_plan = LLM(plan_solution_steps(problem_analysis));
  detailed_solution = LLM(execute_solution(problem, solution_plan));
  verification = LLM(verify_solution(problem, detailed_solution));

  return {
    original_problem: problem,
    analysis: problem_analysis,
    plan: solution_plan,
    solution: detailed_solution,
    verification: verification
  };
}
"""

# --- Tools ---

@mcp.tool()
def get_protocol_shell(intent: str, name: str = "MyProtocol") -> str:
    """
    Returns a blank Protocol Shell structure (Module 05) for defining cognitive tools.

    Args:
        intent: The goal or purpose of this protocol.
        name: The name of the protocol.
    """
    return PROTOCOL_SHELL_STRUCTURE.format(name=name, intent=intent)

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
    if program_type == "math":
        return PROMPT_PROGRAM_MATH_TEMPLATE
    else:
        return f"// Program type '{program_type}' not yet implemented. Returning generic structure.\\n" + PROMPT_PROGRAM_MATH_TEMPLATE

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
