# Sutra Roadmap: From Library to Engine

**Current Status**: `v0.1.0` (Static Templates)
**Target Status**: `v0.2.0` (Dynamic Context Orchestration)

> **Architect's Rationale**: The current implementation allows users to fetch strings. The next phase transforms Sutra into an active participant that generates *runtime protocols* for reasoning (Cognitive Tools) and memory (Cells). We are moving from "Reading" context to "Engineering" it.

---

## Phase 1: The Cognitive Foundry (Thinking Models)
*Objective: Implement structured reasoning primitives based on IBM Research (2025) and Prompt Programming (Module 07).*

- [ ] **Refactor Directory Structure**
    - Move flat `templates.py` into domain-driven structure: `core/`, `systems/`, `cognitive/`.
    - **Rationale**: Separation of concerns between static prompts and dynamic logic.

- [ ] **Implement `cognitive/ibm_tools.py`**
    - [ ] `reasoning.understand_question`: Tool to break down intent/constraints.
    - [ ] `reasoning.backtracking`: Recursive prompt for error correction.
    - [ ] `symbolic.abstract`: Tool to convert tokens to abstract variables (ICML 2025).
    - **Rationale**: Provide "Lego blocks" for logic, not just text generation.

- [ ] **Implement Prompt Program Generator (`core/programs.py`)**
    - [ ] Create `get_prompt_program(type)` builder.
    - [ ] Support "Math Solver" and "Debate" program types.
    - **Rationale**: Enable users to pull executable prompt logic (Module 07).

## Phase 2: The Cell Laboratory (Memory & State)
*Objective: Solve the "Goldfish Memory" problem using Cell Theory (Module 03).*

- [ ] **Implement `core/cells.py`**
    - [ ] `cell.protocol.key_value`: System prompt forcing JSON state updates.
    - [ ] `cell.protocol.windowed`: Logic for sliding window context prompts.
    - [ ] `cell.protocol.episodic`: "Write-only" logs for long-horizon agents.
    - **Rationale**: Context is useless without persistence. These tools inject state management into the user's system prompt.

## Phase 3: The Organ Assembly (Orchestration)
*Objective: Enable multi-agent workflows (Module 04).*

- [ ] **Implement `systems/organs.py`**
    - [ ] `organ.research_synthesis`: The Scout -> Architect -> Scribe pattern.
    - [ ] `organ.debate_council`: Multi-perspective round-robin generator.
    - **Rationale**: Pre-fab architectures reduce the cognitive load on the user to build complex systems from scratch.

## Phase 4: Maintenance & Quality
- [ ] **Add Schema Validators**
    - Create Pydantic models for all Tool inputs/outputs.
- [ ] **Documentation**
    - Auto-generate `README.md` updates based on new Tools.
