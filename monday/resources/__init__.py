"""This is the init file for the resources package."""

from monday.resources.boards import BoardResource
from monday.resources.notifications import NotificationResource
from monday.resources.users import UserResource
from monday.resources.versions import VersionResource
from monday.resources.workspaces import WorkspaceResource

__all__ = [
    "BoardResource",
    "NotificationResource",
    "UserResource",
    "VersionResource",
    "WorkspaceResource",
]
