"""This module provides the Tags class for accessing the Tags endpoint."""

from monday.resources.base import BaseResource
from monday.utils import parse_parameters


class TagResource(BaseResource):
    """Class for interacting with the Monday.com API's Tags endpoint."""

    async def fetch_tags(
        self: "TagResource",
        ids: str | list[str] | None = None,
    ) -> dict:
        """Return metadata about one or a collection of the account's public tags.

        Public tags are the tags that appear on Main Boards, which are accessible to all
        Member and Viewer-level users by default.

        Args:
            ids (str | list(str), optional): A list of tags' identifiers.

        Returns:
            (dict): Dict response from the monday.com GraphQL API.
        """
        parameters = parse_parameters(locals())
        query = f"""query {{
            tags {f"({", ".join(parameters)})" if parameters else ""} {{
                color
                id
                name
            }}
        }}"""

        return await self.client.execute(query)

    async def create_or_get_tag(
        self: "TagResource",
        tag_name: str,
        board_id: str | None = None,
    ) -> dict:
        """Allows you to create new tags or receive their data if they already exist.

        Private and Shareable boards will also have private tags, so if you wish to use
        your tags in a Private or Shareable board, use the board_id argument. No need to
        send this argument when sending mutations to Main boards.

        Args:
            tag_name (str): The new tag's name.
            board_id (str, optional): The Shareable or Private Board ID where the tag
                should be created (not needed for Main boards)

        Returns:
            (dict): Dict response from the monday.com GraphQL API.
        """
        parameters = parse_parameters(locals())
        query = f"""mutation
        {{
            create_or_get_tag {f"({", ".join(parameters)})" if parameters else ""} {{
                name
                color
                id
            }}
        }}"""

        return await self.client.execute(query)
