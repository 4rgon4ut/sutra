"""Organ patterns for multi-agent orchestration (Layer 4).

Organs combine programs and cells into cohesive multi-agent workflows.
Based on the architectural spec from .context/00_foundations/04_organs_applications.md
"""

from typing import Final

ORGAN_DEBATE_COUNCIL: Final[str] = """
/organ.debate_council{{
    intent="Generate balanced analysis through multi-perspective debate",

    input={{
        question="<question_or_topic>",
        perspectives=["Optimistic", "Skeptical", "Pragmatic", "Ethical"],
        rounds=2
    }},

    architecture={{
        pattern="moderator → perspectives → debate_rounds → synthesis",
        components=[
            "Moderator Cell: Frames the question and sets debate parameters",
            "Perspective Cells: Each represents a distinct viewpoint",
            "Debate Rounds: Iterative refinement through dialogue",
            "Synthesis Cell: Integrates all perspectives into coherent conclusion"
        ]
    }},

    process=[
        /phase.moderator{{
            role="Frame the debate",
            actions=[
                "Clarify the core question and any ambiguities",
                "Identify key dimensions of debate",
                "Establish evaluation criteria",
                "Set scope and constraints"
            ],
            output="framing_context"
        }},

        /phase.generate_perspectives{{
            role="Generate initial positions",
            for_each="perspective in perspectives",
            actions=[
                "State core position on the question",
                "Provide 2-3 key supporting arguments",
                "Identify underlying assumptions",
                "Acknowledge limitations or counterarguments"
            ],
            output="initial_perspectives[]"
        }},

        /phase.debate_rounds{{
            role="Conduct multi-round debate",
            iterations="rounds",
            for_each_round=[
                "Each perspective responds to strongest counterarguments",
                "Refine or strengthen position based on discussion",
                "Find areas of agreement or common ground",
                "Raise new considerations not yet addressed"
            ],
            output="debate_history[]"
        }},

        /phase.synthesis{{
            role="Synthesize all perspectives",
            actions=[
                "Summarize each major perspective and key arguments",
                "Identify areas of consensus or common ground",
                "Acknowledge irreconcilable differences and why",
                "Provide nuanced conclusion acknowledging complexity",
                "Generate recommendations or implications"
            ],
            output="final_synthesis"
        }}
    ],

    output={{
        framing="Debate framing and context",
        perspectives="All perspective positions",
        debate_rounds="Full debate history",
        synthesis="Integrated multi-perspective conclusion",
        num_perspectives="Count of perspectives considered",
        num_rounds="Number of debate rounds conducted"
    }},

    meta={{
        organ_type="multi_agent_deliberation",
        layer="organs",
        complexity="medium",
        use_cases=[
            "Complex decision analysis",
            "Policy evaluation",
            "Ethical dilemmas",
            "Strategic planning",
            "Research direction setting"
        ]
    }}
}}
"""


def get_organ_template(organ_name: str) -> str:
    """Return an organ template for orchestrating multi-agent workflows.

    Args:
        organ_name: Identifier for the organ (e.g., "debate_council").

    Returns:
        Template string for the requested organ, or error message if not found.
    """
    normalized_name = organ_name.lower().replace("organ.", "").replace("_", "").replace("-", "")

    # Match debate_council variants
    if normalized_name in ["debatecouncil", "debate", "multiperspective"]:
        return ORGAN_DEBATE_COUNCIL

    # Return helpful error for unknown organs
    available = ["debate_council"]
    return (
        f"// Organ '{organ_name}' not found.\\n"
        f"// Available organs: {', '.join(available)}\\n"
        f"// Returning debate_council as example:\\n\\n"
        + ORGAN_DEBATE_COUNCIL
    )


__all__ = [
    "ORGAN_DEBATE_COUNCIL",
    "get_organ_template",
]
