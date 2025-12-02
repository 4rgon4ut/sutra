"""Core layer modules for Context Engineering (Atoms, Molecules, Programs)."""

from context_engineering_mcp.core.atoms import PROTOCOL_SHELL_STRUCTURE, format_protocol_shell
from context_engineering_mcp.core.molecules import (
    MOLECULAR_CONTEXT_FUNC,
    PROTOCOL_REGISTRY,
    get_protocol_template,
)
from context_engineering_mcp.core.programs import PROMPT_PROGRAM_MATH_TEMPLATE, get_program_template

__all__ = [
    "PROTOCOL_SHELL_STRUCTURE",
    "format_protocol_shell",
    "MOLECULAR_CONTEXT_FUNC",
    "PROTOCOL_REGISTRY",
    "get_protocol_template",
    "PROMPT_PROGRAM_MATH_TEMPLATE",
    "get_program_template",
]
