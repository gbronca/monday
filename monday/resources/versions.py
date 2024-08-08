"""Class for interacting with the Monday.com API's Versions endpoint."""

from monday.resources.base import BaseResource


class VersionResource(BaseResource):
    """Class for interacting with the Monday.com API's Users endpoint."""

    async def fetch_versions(self: "VersionResource") -> dict:
        """Versions will return metadata about all available API versions.

        Returns:
            dict: dict response from the monday.com GraphQL API
        """
        query = """query
        {
            versions {
                kind
                value
                display_name
            }
        }"""

        return await self.client.execute(query)

    async def fetch_version(self: "VersionResource") -> dict:
        """Version will return metadata about the API version used to make a request.

        Returns:
            dict: dict response from the monday.com GraphQL API
        """
        query = """query
        {
            version {
                kind
                value
                display_name
            }
        }"""

        return await self.client.execute(query)
