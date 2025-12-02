"""Prompt program templates (Module 07).

These builders provide pseudo-code structures that guide LLMs through
multi-phase reasoning routines.
"""

from typing import Final

PROMPT_PROGRAM_MATH_TEMPLATE: Final[str] = """
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


def get_program_template(program_type: str) -> str:
    """Return a prompt program template for the requested type.

    Args:
        program_type: Identifier for the program to generate (e.g., "math").

    Returns:
        Template string for the requested program, or a generic message with
        the math solver template when unsupported.
    """
    normalized_type = program_type.lower()
    if normalized_type == "math":
        return PROMPT_PROGRAM_MATH_TEMPLATE
    return (
        f"// Program type '{program_type}' not yet implemented. Returning generic structure.\\n"
        + PROMPT_PROGRAM_MATH_TEMPLATE
    )


__all__ = ["PROMPT_PROGRAM_MATH_TEMPLATE", "get_program_template"]
