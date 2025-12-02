"""Cognitive thinking models and reasoning templates.

These tools generate structured prompts that enforce intent clarification and
logic verification before executing downstream actions.
"""

from typing import Optional

from mcp.server.fastmcp import FastMCP


def register_thinking_models(mcp: FastMCP) -> None:
    """Register cognitive thinking-model tools on the provided MCP instance.

    Args:
        mcp: Active FastMCP instance to attach tools to.
    """

    @mcp.tool()
    def understand_question(
        question: str,
        context: Optional[str] = None,
        constraints: Optional[str] = None,
    ) -> str:
        """Produce a protocol shell to decompose a user question.

        Args:
            question: The raw user ask to unpack.
            context: Optional background knowledge or situational frame.
            constraints: Explicit limits or success criteria.

        Returns:
            A structured prompt guiding the model to restate intent, surface
            constraints, and prepare clarifying questions before acting.
        """

        normalized_context = context or "<none>"
        normalized_constraints = constraints or "<none>"

        template = """
/reasoning.understand_question{{
    intent="Clarify the ask before solving by isolating intent, constraints, and required outputs",
    input={{
        question="{question}",
        context="{context}",
        constraints="{constraints}"
    }},
    process=[
        /intent_map{{action="Restate the core ask and target outcome"}},
        /constraints{{action="List explicit and implicit constraints"}},
        /decomposition{{action="Break request into solvable sub-goals"}},
        /risk_check{{action="Flag ambiguity or missing data"}}
    ],
    output={{
        intent="Single sentence goal statement",
        constraints="Bullet list of must-haves and guardrails",
        clarifications="Questions to close gaps before execution",
        proposed_plan="Initial steps or protocol to proceed"
    }}
}}
"""
        return template.format(
            question=question,
            context=normalized_context,
            constraints=normalized_constraints,
        )

    @mcp.tool()
    def verify_logic(
        claim: str,
        reasoning_trace: str,
        constraints: Optional[str] = None,
    ) -> str:
        """Generate a verification protocol for a reasoning trace.

        Args:
            claim: The headline answer or assertion to validate.
            reasoning_trace: The supporting chain-of-thought or proof steps.
            constraints: Optional guardrails (requirements, risk limits).

        Returns:
            Structured prompt that audits assumptions, inference steps, and
            evidence, then proposes patches for any defects.
        """
        normalized_constraints = constraints or "<none>"

        template = """
/reasoning.verify_logic{{
    intent="Audit a reasoning trace for validity, completeness, and constraint alignment",
    input={{
        claim="{claim}",
        reasoning_trace="{reasoning_trace}",
        constraints="{constraints}"
    }},
    process=[
        /premise_check{{action="List premises and mark which are stated vs. assumed"}},
        /consistency{{action="Check each step for logical validity and missing links"}},
        /evidence_map{{action="Match claims to evidence or note gaps"}},
        /contra{{action="Search for contradictions or constraint violations"}},
        /repair_plan{{action="Suggest minimal edits or extra steps to fix defects"}}
    ],
    output={{
        verdict="pass|fail with one sentence rationale",
        defect_log="Numbered list of issues with locations in the trace",
        patched_plan="Revised steps or guardrails to repair the reasoning",
        confidence="0-1 score grounded in evidence coverage and consistency"
    }}
}}
"""
        return template.format(
            claim=claim,
            reasoning_trace=reasoning_trace,
            constraints=normalized_constraints,
        )


__all__ = ["register_thinking_models"]
