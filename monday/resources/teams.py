"""This module provides the Team class for accessing the Teams endpoint."""

from monday.resources.base import BaseResource
from monday.utils import parse_parameters


class TeamResource(BaseResource):
    """Class for interacting with the Monday.com API's Team endpoint."""

    async def fetch_teams(
        self: "TeamResource",
        ids: str | list[str] | None = None,
    ) -> dict:
        """Return metadata about one or several teams.

        Args:
            ids (str | list(str), optional): The unique identifiers of the
                specific teams to return.

        Returns:
            (dict): Dict response from the monday.com GraphQL API.
        """
        parameters = parse_parameters(locals())
        query = f"""query {{
            teams {f"({", ".join(parameters)})" if parameters else ""} {{
                id
                name
                picture_url
                owners {{
                    ids
                }}
                users {{
                    emails
                    ids
                    kind
                    name
                }}
            }}
        }}"""

        return await self.client.execute(query)
