"""This module provides the Board class for managing boards."""

import json
from typing import Literal, TypedDict, Unpack

from monday.exceptions import ArgumentError
from monday.resources.base import BaseResource


class BoardQuery(TypedDict, total=False):
    """Represents a board with optional attributes."""

    board_kind: Literal["private", "public", "share"]
    ids: list[str] | str
    limit: int
    order_by: Literal["created_at", "used_at"]
    page: int
    state: Literal["active", "all", "archived", "deleted"]
    workspace_ids: list[str] | str


class BoardCreate(TypedDict, total=False):
    """Keyword Arguments for creating a board."""

    board_owner_ids: str | list[str]
    board_subscriber_ids: str | list[str]
    board_subscriber_team_ids: str | list[str]
    description: str
    folder_id: str
    template_id: str
    workspace_id: str


class BoardDuplicate(TypedDict, total=False):
    """Duplicates a board with optional attributes."""

    board_name: str
    workspace_id: str
    folder_id: str
    keep_subscribers: bool


class BoardResource(BaseResource):
    """Represents a resource for querying boards."""

    def fetch_boards(self: "BoardResource", **kwargs: Unpack[BoardQuery]) -> dict:
        """Will return metadata about one or a collection of boards.

        Kwargs:
            board_kind (Literal["private", "public", "share"]): The type of board.
            ids (str | [str]): The specific board IDs to return.
            limit (int): The number of boards to return. The default is 25.
            order_by (Literal["created_at", "used_at"]): The order in which to retrieve
                your boards.
            page (int): The page number to return. Starts at 1.
            state (Literal["active", "all", "archived", "deleted"]): The state of board
                to return. The default is active.
            workspace_ids (str | [str]): The specific workspace IDs that contain the
                boards to return.

        Returns:
            dict: dictionary response from the monday.com GraphQL API
        """
        arguments = []
        if kwargs:
            keys_to_not_dump = {"board_kind", "order_by", "state"}
            arguments = [
                f"{key}: {value if key in keys_to_not_dump else json.dumps(value)}"
                for key, value in kwargs.items()
            ]

        query = """
            query {
                boards %s {
                    id
                    name
                    board_folder_id
                    board_kind
                    communication
                    description
                    items_count
                    item_terminology
                    permissions
                    state
                    type
                    updated_at
                    workspace_id
                    creator {
                        id
                        name
                        email
                    }
                    owners {
                        id
                        name
                        email
                    }
                    subscribers {
                        id
                        name
                        email
                    }
                    groups {
                        id
                        title
                        color
                        position
                    }
                    top_group {
                        id
                        title
                        color
                    }
                    tags {
                        id
                        name
                        color
                    }
                    columns {
                        id
                        title
                        type
                    }
                }
            }
        """ % (f"({", ".join(arguments)})" if arguments else "")

        return self.client.execute(query)

    def create_board(
        self: "BoardResource",
        board_name: str,
        board_kind: Literal["private", "public", "share"],
        **kwargs: Unpack[BoardCreate],
    ) -> dict:
        """Allows you to create a new board via the API.

        Please note that the user that creates the board via the API will automatically
        be added as the board's owner when creating a private or shareable board or if
        the board_owners_ids argument is missing.

        board_kind (Literal[private, public, share]): The type of board to create.
        board_name (str): The new board's name.

        Kwargs:
            board_owner_ids (str | list[str] | None): A list of the IDs of the users who
                will be board owners.
            board_subscriber_ids (str | list[str] | None): A list of the IDs of the
                users who will subscribe to the board.
            board_subscriber_team_ids (str | list[str] | None): A list of the IDs of the
                teams who will subscribe to the board.
            description (str | None): The new board's description.
            folder_id (str | None): The board's folder ID.
            template_id (str | None): The board's template ID.
            workspace_id (str | None): The board's workspace ID.
        """
        arguments = []
        if kwargs:
            convert_to_list = [
                "board_owner_ids",
                "board_subscriber_ids",
                "board_subscriber_team_ids",
            ]
            for arg in convert_to_list:
                if arg in kwargs and not isinstance(kwargs[arg], list):  # type: ignore
                    kwargs[arg] = json.dumps([str(kwargs[arg])])  # type: ignore
                elif arg in kwargs:
                    kwargs[arg] = json.dumps(kwargs[arg])  # type: ignore

            arguments = [
                f"{key}: {value if key in convert_to_list else json.dumps(str(value))}"
                for key, value in kwargs.items()
            ]

        optional_arg = ", ".join(arguments) if arguments else ""
        query = f"""mutation {{
            create_board (
                board_name: "{board_name}", board_kind: {board_kind}, {optional_arg}) {{
                id
            }}
        }}"""

        return self.client.execute(query)

    def duplicate_board(
        self: "BoardResource",
        board_id: str,
        duplicate_type: Literal[
            "duplicate_board_with_structure",
            "duplicate_board_with_pulses",
            "duplicate_board_with_pulses_and_updates",
        ] = "duplicate_board_with_pulses_and_updates",
        **kwargs: Unpack[BoardDuplicate],
    ) -> dict:
        """Allows you to duplicate a board via the API.

        board_id (str): The board ID to duplicate.

        Kwargs:
            board_name (str): The duplicated board's name. Optional.
                If omitted, will be automatically generated.
            duplicate_type (str): The duplication type. The options are:
                duplicate_board_with_structure,
                duplicate_board_with_pulses,
                duplicate_board_with_pulses_and_updates.
                Default is 'duplicate_board_with_pulses_and_updates'.
            workspace_id (str): The destination workspace. Optional.
                If omitted, will default to the original board's workspace.
            folder_id (str): The destination folder within the destination workspace.
                The folder_id is required if you are duplicating to another workspace.
                Optional otherwise. If omitted, will default to the original board's
                folder.
            keep_subscribers (bool): Ability to duplicate the subscribers to the new
                board. Default is False.

        Returns:
            dict: dictionary response from the monday.com GraphQL API
        """
        arguments = []
        if kwargs:
            arguments = [f"{key}: {json.dumps(value)}" for key, value in kwargs.items()]

        if "workspace_id" in kwargs and "folder_id" not in kwargs:
            error = "folder_id is required if you are duplicating to another workspace"
            raise ArgumentError(error)

        query = (
            """
            mutation {
                duplicate_board(
                board_id: "%(board_id)s",
                duplicate_type: %(duplicate_type)s,
                %(arguments)s
            ) {
                board {
                    id
                }
            }
        }"""  # noqa: UP031
            % {
                "board_id": board_id,
                "duplicate_type": duplicate_type,
                "arguments": ", ".join(arguments) if arguments else "",
            }
        )

        return self.client.execute(query)

    def archive_board(self: "BoardResource", board_id: str) -> dict:
        """This method allows you to archive a board.

        Args:
            board_id (str): The board's unique identifier.

        Returns:
            dict: dictionary response from the monday.com GraphQL API
        """
        query = (
            """
            mutation {
                archive_board(board_id: "%s") {
                    id
                }
            }
        """
            % board_id
        )

        return self.client.execute(query)

    def delete_board(self: "BoardResource", board_id: str) -> dict:
        """Allows you to delete a board via the API.

        Args:
            board_id (str): Id of the board to be deleted

        Returns:
            dict: dictionary response from the monday.com GraphQL API
        """
        query = (
            """
            mutation {
                delete_board(board_id: "%s") {
                    id
                }
            }
        """
            % board_id
        )

        return self.client.execute(query)

    def update_board(
        self: "BoardResource",
        board_id: str,
        board_attribute: Literal["name", "description", "communication"],
        new_value: str,
    ) -> dict:
        """Allows you to update a board via the API.

        Args:
            board_id (str): Id of the board to be updated
            board_attribute (str): The board's attribute to update
            new_value (str): The new attribute value.

        Returns:
            dict: dictionary response from the monday.com GraphQL API
        """
        query = f""" mutation {{
            update_board(
                board_id: {json.dumps(board_id)},
                board_attribute: {board_attribute},
                new_value: {json.dumps(new_value)})
        }}"""

        print(query)
        return {"id": "123"}
        # return self.client.execute(query)
