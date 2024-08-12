"""This module provides the Team class for accessing the Teams endpoint."""

from typing import Literal

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

    async def add_teams_to_board(
        self: "TeamResource",
        board_id: str,
        team_ids: str | list[str],
        kind: Literal["subscriber", "owner"] | None = None,
    ) -> dict:
        """Allows you to add teams to a board via the API.

        Args:
            board_id (str): The board's unique identifier.
            team_ids (str | list(str)): The unique identifiers of the teams to add to
                the board. You can pass -1 to subscribe everyone in an account to
                the board
            kind (str, option): The team's role: subscriber or owner. If the argument
                is not used, the team will be added as a subscriber.

        Returns:
            (dict): Dict response from the monday.com GraphQL API.
        """
        parameters = parse_parameters(locals())
        query = f"""mutation {{
            add_teams_to_board ({", ".join(parameters)}) {{
                id
            }}
        }}"""

        return await self.client.execute(query)
