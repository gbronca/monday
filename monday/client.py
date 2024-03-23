"""Client for the Monday.com API."""

from .__version__ import __version__
from .resources import (
    UserResource,
    VersionResource,
)


class MondayClient:
    """Client for the Monday.com API."""

    def __init__(  # noqa: D107
        self: "MondayClient",
        api_key: str,
        api_version: str | None = None,
    ) -> None:
        self.users = UserResource(api_key=api_key, api_version=api_version)
        self.versions = VersionResource(api_key=api_key, api_version=api_version)

    def __repr__(self: "MondayClient") -> str:  # noqa: D105
        return f"MondayClient {__version__}"

    def __str__(self: "MondayClient") -> str:  # noqa: D105
        return f"MondayClient {__version__}"
