"""BaseResource class for Monday.com API."""
from monday.graphql.client import GraphQLClient

URLS = {
    "prod": "https://api.monday.com/v2",
    "file": "https://api.monday.com/v2/file",
}


class BaseResource:
    """BaseResource class for Monday.com API."""

    def __init__(
        self: "BaseResource",
        api_key: str,
        api_version: str | None = None,
    ) -> None:
        self.api_key = api_key
        self.api_version = api_version
        self.client = GraphQLClient(
            endpoint=URLS["prod"],
            api_key=api_key,
            api_version=api_version,
        )
        self.client_file_upload = GraphQLClient(
            endpoint=URLS["file"],
            api_key=api_key,
            api_version=api_version,
        )

    def __str__(self: "BaseResource") -> str:  # noqa: D105
        return self.__class__.__name__

    def __repr__(self: "BaseResource") -> str:  # noqa: D105
        return self.__class__.__name__
