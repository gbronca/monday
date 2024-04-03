"""Describe the types for the boards resource."""

from typing import Literal, TypedDict


class Workspace(TypedDict, total=False):
    """Represents a workspace with optional attributes."""

    ids: list[str] | str
    kind: Literal["open", "closed"]
    limit: int
    state: Literal["all", "active", "archived", "deleted"]
    order_by: Literal["created_at"]
    page: int
