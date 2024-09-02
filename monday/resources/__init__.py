"""This is the init file for the resources package."""

from monday.resources.boards import BoardResource
from monday.resources.columns import ColumnResource
from monday.resources.notifications import NotificationResource
from monday.resources.tags import TagResource
from monday.resources.teams import TeamResource
from monday.resources.updates import UpdateResource
from monday.resources.users import UserResource
from monday.resources.versions import VersionResource
from monday.resources.webhooks import WebhookResource
from monday.resources.workspaces import WorkspaceResource

__all__ = [
    "BoardResource",
    "ColumnResource",
    "NotificationResource",
    "TagResource",
    "TeamResource",
    "UpdateResource",
    "UserResource",
    "VersionResource",
    "WebhookResource",
    "WorkspaceResource",
]
