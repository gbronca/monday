"""This module provides the Group class for accessing the Groups endpoint."""

import json
from typing import Literal

from src.monday.utils import parse_parameters

from .base import BaseResource
from .types.types import GroupColor


class GroupResource(BaseResource):
    """Class for interacting with the Monday.com API's Group endpoint."""

    async def fetch_groups(
        self: "GroupResource",
        board_ids: str | list[str],
        group_ids: str | list[str] | None = None,
    ) -> dict:
        """Allows you to query one or a collection of groups on a specific board.

        Args:
            board_ids (str | [str]): The board's identifier.
            group_ids (str, optional): The group's identifier.

        Returns:
            (dict): dict object with the response from the API
        """
        parameters = parse_parameters(locals())

        query = f"""query {{
            boards (ids: {json.dumps(board_ids)}) {{
                groups {f"(ids: {json.dumps(group_ids)})" if group_ids else ""} {{
                    archived
                    color
                    deleted
                    id
                    position
                    title
                }}
                id
                name
            }}
        }}"""

        return await self.client.execute(query)

    async def create_group(
        self: "GroupResource",
        board_id: str,
        group_name: str,
        relative_to: str | None = None,
        position_relative_method: Literal["before_at", "after_at"] | None = None,
        group_color: GroupColor | None = None,
    ) -> dict:
        """Allows you to creates a new empty group.

        Args:
            board_id (str): The board's identifier.
            group_name (str): The name of the new group.
            group_color (str, optional): The group's HEX code color.
            relative_to (str): The unique identifier of the group you want to create
                the new one in relation to. The default creates the new group below
                the specified group_id.
                You can also use this argument in conjunction with
                position_relative_group to specify if you want to create the new group
                above or below the group in question.
            position_relative_method (str, optional): The desired position of the new
                group.
                You can use this argument in conjunction with relative_to to specify
                which group you want to create the new group above or below.
                before_at: This enum value creates the new group above the relative_to
                value. If you don't use the relative_to argument, the new group will
                be created at the bottom of the board.
                after_at: This enum value creates the new group below the relative_to
                value. If you don't use the relative_to argument, the new group will be
                created at the top of the board.

        Returns:
            (dict): dict object with the response from the API
        """
        parameters = parse_parameters(
            locals(),
            literals=["position_relative_method", "group_color"],
        )

        query = f"""mutation {{
            create_group ({", ".join(parameters)}) {{
                id
            }}
        }}"""

        return await self.client.execute(query)

    async def update_group(
        self: "GroupResource",
        board_id: str,
        group_id: str,
        group_attribute: Literal[
            "color",
            "position",
            "relative_position_after",
            "relative_position_before",
            "title",
        ],
        new_value: str,
    ) -> dict:
        """Allows you to update an existing group.

        Args:
            board_id (str): The board's unique identifier.
            group_id (str): The group's unique identifier.
            group_attribute (str): The group attribute that you want to update.
                The available attributes are
                - title
                - color.
                - relative_position_after
                - relative_position_before
            new_value (str): The new attribute value.

        Returns:
            (dict): dict object with the response from the API
        """
        parameters = parse_parameters(locals(), literals=["group_attribute"])
        query = f"""mutation {{
            update_group ({", ".join(parameters)}) {{
                id
            }}
        }}"""

        return await self.client.execute(query)

    async def duplicate_group(
        self: "GroupResource",
        board_id: str,
        group_id: str,
        group_title: str | None = None,
        add_to_top: bool | None = None,
    ) -> dict:
        """Allows you to duplicate a group with all of its items.

        Args:
            board_id (str): The board's unique identifier.
            group_id (str): The group's unique identifier.
            group_title (str, optional): The group's title.
            add_to_top (bool): Boolean to add new group to the top of the board.

        Returns:
            (dict): dict object with the response from the API
        """
        parameters = parse_parameters(locals())
        query = f"""mutation {{
            duplicate_group ({", ".join(parameters)}) {{
                id
            }}
        }}"""

        return await self.client.execute(query)

    async def move_item_to_group(
        self: "GroupResource",
        group_id: str,
        item_id: str,
    ) -> dict:
        """Allows you to move an item between groups on the same board.

        Args:
            group_id (str): The group's unique identifier.
            item_id (str): The item's unique identifier.

        Returns:
            (dict): dict object with the response from the API
        """
        parameters = parse_parameters(locals())
        query = f"""mutation {{
            move_item_to_group ({", ".join(parameters)}) {{
                id
            }}
        }}"""

        return await self.client.execute(query)

    async def archive_group(
        self: "GroupResource",
        board_id: str,
        group_id: str,
    ) -> dict:
        """Allows you to archive a group with all of its items.

        Args:
            board_id (str): The board's unique identifier.
            group_id (str): The group's unique identifier.

        Returns:
            (dict): dict object with the response from the API
        """
        parameters = parse_parameters(locals())
        query = f"""mutation {{
            archive_group ({", ".join(parameters)}) {{
                id
            }}
        }}"""

        return await self.client.execute(query)

    async def delete_group(
        self: "GroupResource",
        board_id: str,
        group_id: str,
    ) -> dict:
        """Allows you to delete a group with all of its items.

        Args:
            board_id (str): The board's unique identifier.
            group_id (str): The group's unique identifier.

        Returns:
            (dict): dict object with the response from the API
        """
        parameters = parse_parameters(locals())
        query = f"""mutation {{
            delete_group ({", ".join(parameters)}) {{
                id
                deleted
            }}
        }}"""

        return await self.client.execute(query)
