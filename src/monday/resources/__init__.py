"""This is the init file for the resources package."""

from .boards import BoardResource
from .columns import ColumnResource
from .folders import FolderResource
from .groups import GroupResource
from .notifications import NotificationResource
from .tags import TagResource
from .teams import TeamResource
from .updates import UpdateResource
from .users import UserResource
from .versions import VersionResource
from .webhooks import WebhookResource
from .workspaces import WorkspaceResource

__all__ = [
    "BoardResource",
    "ColumnResource",
    "FolderResource",
    "GroupResource",
    "NotificationResource",
    "TagResource",
    "TeamResource",
    "UpdateResource",
    "UserResource",
    "VersionResource",
    "WebhookResource",
    "WorkspaceResource",
]
