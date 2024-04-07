"""Module description goes here."""

from typing import Literal, TypedDict


class User(TypedDict, total=False):
    """Represents a user with optional attributes."""

    emails: list[str] | str
    ids: list[str] | str
    kind: Literal["all", "non_guests", "guests", "non_pending"]
    limit: int
    name: str
    newest_first: bool
    non_active: bool
    page: int
