# Protocol Shells extracted from CLAUDE.md

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

REASONING_SYSTEMATIC = """
/reasoning.systematic{
    intent="Break down complex problems into logical steps with traceable reasoning",
    input={
        problem="<problem_statement>",
        constraints="<constraints>",
        context="<context>"
    },
    process=[
        /understand{action="Restate problem and clarify goals"},
        /analyze{action="Break down into components"},
        /plan{action="Design step-by-step approach"},
        /execute{action="Implement solution methodically"},
        /verify{action="Validate against requirements"},
        /refine{action="Improve based on verification"}
    ],
    output={
        solution="Implemented solution",
        reasoning="Complete reasoning trace",
        verification="Validation evidence"
    }
}
"""

THINKING_EXTENDED = """
/thinking.extended{
    intent="Engage deep, thorough reasoning for complex problems requiring careful consideration",
    input={
        problem="<problem_requiring_deep_thought>",
        level="<basic|deep|deeper|ultra>" // Corresponds to think, think hard, think harder, ultrathink
    },
    process=[
        /explore{action="Consider multiple perspectives and approaches"},
        /evaluate{action="Assess trade-offs of each approach"},
        /simulate{action="Test mental models against edge cases"},
        /synthesize{action="Integrate insights into coherent solution"},
        /articulate{action="Express reasoning clearly and thoroughly"}
    ],
    output={
        conclusion="Well-reasoned solution",
        rationale="Complete thinking process",
        alternatives="Other considered approaches"
    }
}
"""

WORKFLOW_TDD = """
/workflow.test_driven{
    intent="Implement changes using test-first methodology",
    input={
        feature="<feature_to_implement>",
        requirements="<detailed_requirements>"
    },
    process=[
        /write_tests{
            action="Create comprehensive tests based on requirements",
            instruction="Don't implement functionality yet"
        },
        /verify_tests_fail{
            action="Run tests to confirm they fail appropriately",
            instruction="Validate test correctness"
        },
        /implement{
            action="Write code to make tests pass",
            instruction="Focus on passing tests, not implementation elegance initially"
        },
        /refactor{
            action="Clean up implementation while maintaining passing tests",
            instruction="Improve code quality without changing behavior"
        },
        /finalize{
            action="Commit both tests and implementation",
            instruction="Include test rationale in commit message"
        }
    ],
    output={
        tests="Comprehensive test suite",
        implementation="Working code that passes tests",
        commit="Commit message and PR details"
    }
}
"""

CODE_ANALYZE = """
/code.analyze{
    intent="Deeply understand code structure, patterns and quality",
    input={
        code="<code_to_analyze>",
        focus="<specific_aspects_to_examine>"
    },
    process=[
        /parse{
            structure="Identify main components and organization",
            patterns="Recognize design patterns and conventions",
            flow="Trace execution and data flow paths"
        },
        /evaluate{
            quality="Assess code quality and best practices",
            performance="Identify potential performance issues",
            security="Spot potential security concerns",
            maintainability="Evaluate long-term maintainability"
        },
        /summarize{
            purpose="Describe the code's primary functionality",
            architecture="Outline architectural approach",
            interfaces="Document key interfaces and contracts"
        }
    ],
    output={
        overview="High-level summary of the code",
        details="Component-by-component breakdown",
        recommendations="Suggested improvements"
    }
}
"""

PROJECT_EXPLORE = """
/project.explore{
    intent="Build comprehensive understanding of project structure",
    input={
        repo="<repository_path>",
        focus="<exploration_objectives>"
    },
    process=[
        /scan{
            structure="Map directory hierarchy",
            files="Identify key files",
            patterns="Recognize organizational patterns"
        },
        /analyze{
            architecture="Determine architectural approach",
            components="Identify main components",
            dependencies="Map component relationships"
        },
        /document{
            overview="Create high-level summary",
            components="Document key components",
            patterns="Describe recurring patterns"
        }
    ],
    output={
        map="Structural representation of codebase",
        key_areas="Identified important components",
        entry_points="Recommended starting points"
    }
}
"""

PROTOCOL_REGISTRY = {
    "reasoning.systematic": REASONING_SYSTEMATIC,
    "thinking.extended": THINKING_EXTENDED,
    "workflow.test_driven": WORKFLOW_TDD,
    "code.analyze": CODE_ANALYZE,
    "project.explore": PROJECT_EXPLORE
}
