"""Client for the Monday.com API."""

from .__version__ import __version__
from .resources import (
    BoardResource,
    NotificationResource,
    UserResource,
    VersionResource,
    WorkspaceResource,
)


class MondayClient:
    """Client for the Monday.com API."""

    def __init__(  # noqa: D107
        self: "MondayClient",
        api_key: str,
        api_version: str | None = None,
    ) -> None:
        self.boards = BoardResource(api_key=api_key, api_version=api_version)
        self.notifications = NotificationResource(
            api_key=api_key,
            api_version=api_version,
        )
        self.users = UserResource(api_key=api_key, api_version=api_version)
        self.versions = VersionResource(api_key=api_key, api_version=api_version)
        self.workspaces = WorkspaceResource(api_key=api_key, api_version=api_version)

    def __repr__(self: "MondayClient") -> str:  # noqa: D105
        return f"MondayClient {__version__}"

    def __str__(self: "MondayClient") -> str:  # noqa: D105
        return f"MondayClient {__version__}"
