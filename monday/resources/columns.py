"""Class for interacting with the Monday.com API's columns endpoint."""

import json

from monday.resources.base import BaseResource
from monday.resources.types.types import ColumnType
from monday.utils import parse_parameters


class ColumnResource(BaseResource):
    """Class for interacting with the Monday.com API's columns endpoint."""

    async def fetch_columns(
        self: "ColumnResource",
        board_ids: list[str] | str,
        column_ids: list[str] | str | None = None,
        types: ColumnType | None = None,
    ) -> dict:
        """Return metadata about one or a collection of columns.

        You can only query columns by nesting it within another query,
        so it can't be used at the root.

        Args:
            board_ids (str | [str]): The board's unique identifier.
            column_ids (str | [str]): The column's unique identifier.
            types (str): The column's type.
        """
        parameters = parse_parameters(
            locals(),
            literals=["types"],
            exclude=["board_ids"],
        )

        query = f"""query {{
            boards(ids: {json.dumps(board_ids)}) {{
                columns {f"({", ".join(parameters)})" if parameters else ""} {{
                    id
                    title
                    archived
                    description
                    settings_str
                    type
                    width
                }}
            }}
        }}"""

        return await self.client.execute(query)

    async def create_column(
        self: "ColumnResource",
        board_id: str,
        title: str,
        column_type: ColumnType,
        after_column_id: str | None = None,
        defaults: dict | None = None,
        description: str | None = None,
        id: str | None = None,  # noqa: A002
    ) -> dict:
        """Allows you to create a new column on a board within the account.

        board_id (str): The board's unique identifier.
        title (str): The new column's title.
        column_type (str): The type of column to create.
        description (str): The column's description.
        after_column_id (str, optional): The unique identifier of the column after
            which the new column will be created.
        defaults (dict, optional): a dict containing the new column's defaults.
            e.g. {"labels":{"1": "Information technology", "2": "Human resources"}}
        id (str, optional): The column's user-specified unique identifier. Please note
            that the mutation will fail if it does not meet any of the following
            requirements:
            - [1-20] characters in length (inclusive)
            - Only lowercase letters (a-z) and underscores (_)
            - Must be unique (no other column on the board can have the same ID)
            - Can't reuse column IDs, even if the column has been deleted from the board
            - Can't be null, blank, or an empty string

        Returns:
            (dict): dict object with the response from the API
        """
        parameters = parse_parameters(locals(), literals=["column_type"])

        query = f"""mutation {{
            create_column ({", ".join(parameters)}) {{
                id
                title
            }}
        }}"""

        return await self.client.execute(query)

    async def change_column_value(
        self: "ColumnResource",
        board_id: str,
        column_id: str,
        value: str | dict,
        item_id: str | None = None,
        *,
        create_labels_if_missing: bool = False,
    ) -> dict:
        """Allows you to change the value of a column in a specific item (row).

        Args:
            board_id (str): The board identifier.
            column_id (str): The column identifier on your board.
            item_id (str): The item's identifier.
            value (str | dict): The new value of the column. The value will be
                converted to JSON.
            create_labels_if_missing (bool): Creates status/dropdown labels if they
                are missing. Requires permission to change the board structure.

        Example:
            change_column_value(
                board_id: "20178755",
                item_id: "200819371",
                column_id: "status",
                value: "{"index": 1}"
            )

        Returns:
            (dict): dict object with the response from the API
        """
        parameters = parse_parameters(locals())
        query = f"""mutation {{
            change_column_value({", ".join(parameters)}) {{
                id
                name
                column_values {{
                    id
                    text
                    value
                }}
            }}
        }}"""

        return await self.client.execute(query)
