"""This module provides the Item class for managing items."""

from src.monday.utils import parse_parameters

from .base import BaseResource


class ItemResource(BaseResource):
    """Class for interacting with the Monday.com API's Items endpoint."""

    async def fetch_items_page(
        self,
        board_ids: list[str] | str,
        cursor: str | None = None,
        limit: int = 25,
        query_params: dict | None = None,
    ) -> dict:
        """Querying items_page return items filtered by the specified criteria.

        You can only query items_page by nesting it within a boards query,
        so it can't be used at the root.

        Args:
            board_ids (str | [str]): The boards' unique identifier.
            limit (int, optional): The number of items to return.
                The default is 25, but the maximum is 500.
            cursor (str, optional): An opaque token representing the position in a set
                of results to fetch items from. Use this to paginate through large
                result sets. Please note that you can't use query_params and cursor in
                the same request. We recommend using query_params for the initial
                request and cursor for paginated requests.
            query_params (str(dict), optional): A set of parameters to filter, sort, and
                control the scope of the boards query. Use this to customize the results
                based on specific criteria. Please note that you can't use query_params
                and cursor in the same request. We recommend using query_params for the
                initial request and cursor for paginated requests.

        Returns:
            dict: dictionary response from the monday.com GraphQL API
        """
        parameters = parse_parameters(locals(), exclude=[board_ids])

        query = f"""query {{
            boards (ids: {board_ids}) {{
                items_page ({parameters}) {{
                    cursor
                    items {{
                        id
                        name
                        created_at
                        relative_link
                        state
                        updated_at

                        board {{
                            id
                            name
                        }}
                        subitems {{
                            id
                            name
                        }}
                        subscribers {{
                            id
                            name
                            email
                        }}
                        group {{
                            id
                            title
                        }}
                        updates {{
                            id
                        }}
                        column_values {{
                            id
                            value
                            text
                        }}
                    }}
                }}
                id
                name
            }}
        }}"""

        return await self.client.execute(query)

    async def fetch_next_items_page(self, cursor: str, limit: int = 25) -> dict:
        """Return the next set of items that correspond with the provided cursor.

        Args:
            cursor (str): An opaque cursor that represents the position in the list
                after the last returned item. Use this cursor for pagination to fetch
                the next set of items. If the cursor is null, there are no more items
                to fetch.
            limit (int, optional): The number of items to return. The default is 25.
                The maximum is 500.

        Returns:
            dict: dictionary response from the monday.com GraphQL API
        """
        parameters = parse_parameters(locals())
        query = f"""query {{
            next_items_page ({parameters}) {{
                cursor
                items {{
                    id
                    name
                    created_at
                    relative_link
                    state
                    updated_at

                    board {{
                        id
                        name
                    }}
                    subitems {{
                        id
                        name
                    }}
                    subscribers {{
                        id
                        name
                        email
                    }}
                    group {{
                        id
                        title
                    }}
                    updates {{
                        id
                    }}
                    column_values {{
                        id
                        value
                        text
                    }}
                }}
            }}
        }}"""

        return await self.client.execute(query)
