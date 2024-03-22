"""This is the init file for the resources package."""

from monday.resources.users import UserResource
from monday.resources.versions import VersionResource

__all__ = ["UserResource", "VersionResource"]
