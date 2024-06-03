"""Describe the types for the boards resource."""

from typing import Literal, TypedDict

from monday.resources.types.generic_types import State


class WorkspaceKind(TypedDict, total=False):
    """The kind of workspaces."""

    kind: Literal["open", "closed"] | None


class _TWorkspace(TypedDict, total=False):
    """Represents a workspace with optional attributes."""

    ids: list[str] | str
    limit: int
    # state: Literal["all", "active", "archived", "deleted"]
    order_by: Literal["created_at"]
    page: int


class Workspace(_TWorkspace, WorkspaceKind, State):
    """Represents a workspace with optional attributes and kind."""

    pass
