import json

from monday.resources.base import BaseResource
from monday.resources.types.columns import ColumnType


class ColumnResource(BaseResource):
    """Class for interacting with the Monday.com API's columns endpoint."""

    def fetch_columns(
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
            types (ColumnType): The column's type.
        """
        column_args: list[str] = []

        if column_ids:
            column_args.append(f"ids: {json.dumps(column_ids)}")
        if types:
            column_args.append(f"types: {types}")
        column_arguments = f"({', '.join(column_args)})" if column_args else ""

        query = f"""query {{
            boards(ids: {json.dumps(board_ids)}) {{
                columns {column_arguments} {{
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

        return self.client.execute(query)
