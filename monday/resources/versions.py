"""Class for interacting with the Monday.com API's Versions endpoint."""

from monday.resources.base import BaseResource


class VersionResource(BaseResource):
    """Class for interacting with the Monday.com API's Users endpoint."""

    def fetch_version(self: "VersionResource") -> dict:
        """Querying versions will return metadata about all available API versions.

        This method does not accept any arguments and returns an array

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

        return self.client.execute(query)
