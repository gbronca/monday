"""This module provides the Board class for managing boards."""

from src.monday.utils import parse_parameters

from .base import BaseResource
from .types.types import BoardAttributes, BoardKind, DuplicateBoardType, OrderBy, State


class BoardResource(BaseResource):
    """Represents a resource for querying boards."""

    async def fetch_boards(
        self: "BoardResource",
        ids: list[str] | str,
        board_kind: BoardKind | None = None,
        limit: int | None = None,
        order_by: OrderBy | None = None,
        page: int | None = None,
        state: State | None = None,
        workspace_ids: list[str] | str | None = None,
    ) -> dict:
        """Will return metadata about one or a collection of boards.

        Kwargs:
            ids (str | [str]): The specific board IDs to return.
            board_kind (str, optional): The type of board to return.
            limit (int, optional): The number of boards to return. The default is 25.
            order_by (str, optional): The order in which to retrieve your boards.
            page (int, optional): The page number to return. Starts at 1.
            state (str, optional):The state of board to return. The default is active.
            workspace_ids (str | [str], optional): The specific workspace IDs that
                contain the boards to return.

        Returns:
            dict: dictionary response from the monday.com GraphQL API
        """
        parameters = parse_parameters(
            locals(),
            literals=["board_kind", "order_by", "state"],
        )

        query = f"""query {{
            boards {f"({", ".join(parameters)})" if parameters else ""} {{
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
                columns {{
                    id
                    title
                    type
                }}
                creator {{
                    id
                    name
                    email
                }}
                groups {{
                    id
                    title
                    color
                    position
                }}
                owners {{
                    id
                    name
                    email
                }}
                subscribers {{
                    id
                    name
                    email
                }}
                tags {{
                    id
                    name
                    color
                }}
                top_group {{
                    id
                    title
                    color
                }}
            }}
        }}"""

        return await self.client.execute(query)

    async def create_board(
        self: "BoardResource",
        board_name: str,
        board_kind: BoardKind,
        board_owner_ids: str | list[str] | None = None,
        board_subscriber_ids: str | list[str] | None = None,
        board_subscriber_team_ids: str | list[str] | None = None,
        description: str | None = None,
        folder_id: str | None = None,
        template_id: str | None = None,
        workspace_id: str | None = None,
    ) -> dict:
        """Allows you to create a new board.

        Please note that the user that creates the board via the API will automatically
        be added as the board's owner when creating a private or shareable board or if
        the board_owners_ids argument is missing.

        board_name (str): The new board's name.
        board_kind (str): The type of board to create.
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
        parameters = parse_parameters(locals(), literals=["board_kind"])

        query = f"""mutation {{
            create_board ({", ".join(parameters)}) {{
                id
            }}
        }}"""

        return await self.client.execute(query)

    async def duplicate_board(
        self: "BoardResource",
        board_id: str,
        duplicate_type: DuplicateBoardType = "duplicate_board_with_pulses_and_updates",
        board_name: str | None = None,
        folder_id: str | None = None,
        workspace_id: str | None = None,
        *,
        keep_subscribers: bool = False,
    ) -> dict:
        """Allows you to duplicate a board with all of its items and groups.

        board_id (str): The board ID to duplicate.
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
        parameters = parse_parameters(locals(), literals=["duplicate_type"])

        query = f"""mutation {{
            duplicate_board ({", ".join(parameters)}) {{
                board {{
                    id
                }}
            }}
        }}"""

        return await self.client.execute(query)

    async def update_board(
        self: "BoardResource",
        board_id: str,
        board_attribute: BoardAttributes,
        new_value: str,
    ) -> dict:
        """Allows you to update a board via the API.

        board_id (str): Id of the board to be updated
        board_attribute (str): The board's attribute to update
        new_value (str): The new attribute value.

        Returns:
            dict: dictionary response from the monday.com GraphQL API
        """
        parameters = parse_parameters(locals(), literals=["board_attribute"])
        query = f""" mutation {{
            update_board ({", ".join(parameters)})
        }}"""

        return await self.client.execute(query)

    async def archive_board(self: "BoardResource", board_id: str) -> dict:
        """This method allows you to archive a board.

        board_id (str): The board's unique identifier.

        Returns:
            dict: dictionary response from the monday.com GraphQL API
        """
        parameters = parse_parameters(locals())
        query = f"""mutation {{
            archive_board ({", ".join(parameters)}) {{
                id
            }}
        }}"""

        return await self.client.execute(query)

    async def delete_board(self: "BoardResource", board_id: str) -> dict:
        """Allows you to delete a board via the API.

        board_id (str): Id of the board to be deleted

        Returns:
            dict: dictionary response from the monday.com GraphQL API
        """
        parameters = parse_parameters(locals())
        query = f"""mutation {{
            delete_board ({", ".join(parameters)}) {{
                id
            }}
        }}"""

        return await self.client.execute(query)
