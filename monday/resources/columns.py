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
        print(query)
        # return {"query": "query"}
        return await self.client.execute(query)
