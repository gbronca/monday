"""Describe the types for the boards resource."""

from typing import Literal, TypedDict


class BoardQuery(TypedDict, total=False):
    """Represents a board with optional attributes."""

    board_kind: Literal["private", "public", "share"]
    ids: list[str] | str
    limit: int
    order_by: Literal["created_at", "used_at"]
    page: int
    state: Literal["active", "all", "archived", "deleted"]
    workspace_ids: list[str] | str


class BoardCreate(TypedDict, total=False):
    """Keyword Arguments for creating a board."""

    board_owner_ids: str | list[str]
    board_subscriber_ids: str | list[str]
    board_subscriber_team_ids: str | list[str]
    description: str
    folder_id: str
    template_id: str
    workspace_id: str


class BoardDuplicate(TypedDict, total=False):
    """Duplicates a board with optional attributes."""

    board_name: str
    workspace_id: str
    folder_id: str
    keep_subscribers: bool
