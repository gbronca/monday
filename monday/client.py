"""Client for the Monday.com API."""

from .resources import (
    BoardResource,
    ColumnResource,
    FolderResource,
    GroupResource,
    NotificationResource,
    TagResource,
    TeamResource,
    UpdateResource,
    UserResource,
    VersionResource,
    WebhookResource,
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
        self.columns = ColumnResource(api_key=api_key, api_version=api_version)
        self.folders = FolderResource(api_key=api_key, api_version=api_version)
        self.groups = GroupResource(api_key=api_key, api_version=api_version)
        self.notifications = NotificationResource(
            api_key=api_key,
            api_version=api_version,
        )
        self.tags = TagResource(api_key=api_key, api_version=api_version)
        self.teams = TeamResource(api_key=api_key, api_version=api_version)
        self.updates = UpdateResource(api_key=api_key, api_version=api_version)
        self.users = UserResource(api_key=api_key, api_version=api_version)
        self.versions = VersionResource(api_key=api_key, api_version=api_version)
        self.webhooks = WebhookResource(api_key=api_key, api_version=api_version)
        self.workspaces = WorkspaceResource(api_key=api_key, api_version=api_version)

    # def __repr__(self: "MondayClient") -> str:  # noqa: D105
    #     return f"MondayClient {__version__}"

    # def __str__(self: "MondayClient") -> str:  # noqa: D105
    #     return f"MondayClient {__version__}"
