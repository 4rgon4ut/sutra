# Sutra Quickstart

## TL;DR
Unsure which tool to use? Query the **Librarian**:
> "List available context engineering tools."
> *System calls `get_technique_guide()`*

---

## 1. The Stack (Templates)
Sutra exposes a hierarchy of cognitive structures, ranging from atomic prompts to full protocol shells.

### Molecules (Patterns)
Composable, few-shot structures.
*   **`get_molecular_template`**: Dynamic construction of Input/Output or CoT few-shot prompts.
*   **`get_cot_molecules`**: Standard Chain-of-Thought reasoning patterns.

### Cells (Programs)
Pseudo-code definitions for algorithmic reasoning.
*   **`get_prompt_program(type="math")`**: Function-based approach to logical problem solving.

### Organs (Protocols)
Complete, structured workflows (Intent -> Process -> Output).
*   **`code.analyze`**: Structural analysis and quality assessment.
*   **`project.explore`**: Repository mapping and architecture discovery.
*   **`reasoning.systematic`**: Step-by-step logical decomposition.
*   **`workflow.test_driven`**: Strict Test-Driven Development (TDD) cycle.

## 2. Usage Flow
1.  **Discover**: Request the tool registry via `get_technique_guide()`.
2.  **Load**: Request a specific structure (e.g., "Load the TDD protocol").
3.  **Execute**: The LLM instantiates the template with your specific task context.

> **Note:** For automatic selection, describe your task and let the **Router** (`analyze_task_complexity`) determine the optimal complexity level.
