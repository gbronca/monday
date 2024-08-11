"""Class for interacting with the Monday.com API's Updates endpoint."""

from monday.resources.base import BaseResource
from monday.utils import parse_parameters


class UpdateResource(BaseResource):
    """Class for interacting with the Monday.com API's Updates endpoint."""

    async def fetch_updates(
        self: "UpdateResource",
        ids: str | list[str] | None = None,
        limit: int | None = 25,
        page: int | None = None,
    ) -> dict:
        """This method allows you to query updates.

        It can return one or a collection of updates.

        Args:
            ids (str, list[str] | None): The specific ID(s) to return updates for
            limit (int | None): The number of updates to get, the default is 25.
            page (int | None): Page number to get, starting at 1.

        Returns:
            (dict): dict object with the response from the API
        """
        parameters = parse_parameters(locals())
        query = f"""query
        {{
            updates {f"({", ".join(parameters)})" if parameters else ""} {{
                id
                body
                created_at
                creator {{
                    name
                    id
                }}
            }}
        }}"""

        return await self.client.execute(query)

    async def create_update(
        self: "UpdateResource",
        item_id: str,
        body: str,
        parent_id: str | None = None,
    ) -> dict:
        """Creates an update for a specific item (row).

        Args:
            item_id (str): The item's unique identifier.
            body (str): The update's text.
            parent_id (str): The parent update's unique identifier.
                This can be used to create a reply to an update.

        Returns:
            (dict): dict object with the response from the API
        """
        parameters = parse_parameters(locals())
        query = f"""mutation
        {{
            create_update {f"({", ".join(parameters)})" if parameters else ""} {{
                id
            }}
        }}"""

        return await self.client.execute(query)

    async def like_update(self: "UpdateResource", update_id: str) -> dict:
        """Allows you to like an update via the API.

        Args:
            update_id (str): The unique identifier of the update to like.

        Returns:
            (dict): dict object with the response from the API
        """
        parameters = parse_parameters(locals())
        query = f"""
            mutation {{
                like_update ({", ".join(parameters)}) {{
                    id
                }}
            }}
        """

        return await self.client.execute(query)

    async def clear_item_updates(self: "UpdateResource", item_id: str) -> dict:
        """Clear all updates on a specific item, including replies and likes.

        Args:
            item_id (str): The item's unique identifier.

        Returns:
            (dict): dict object with the response from the API
        """
        parameters = parse_parameters(locals())
        query = f"""mutation
        {{
            clear_item_updates ({", ".join(parameters)}) {{
                id
            }}
        }}"""

        return await self.client.execute(query)

    async def delete_update(self: "UpdateResource", update_id: str) -> dict:
        """Allows you to delete an update of an item.

        Args:
            update_id (str): The update's unique identifier.

        Returns:
            (dict): dict object with the response from the API
        """
        parameters = parse_parameters(locals())
        query = f"""
            mutation {{
                delete_update ({", ".join(parameters)}) {{
                    id
                }}
            }}
        """

        return await self.client.execute(query)

    async def add_file_to_update(
        self: "UpdateResource",
        update_id: str,
        file: str,
    ) -> dict:
        """Adds a file to an update.

        Args:
            update_id (str): Id of the update to be updated
            file (str): Path to the file to be added

        Returns:
            (dict): dict object with the response from the API
        """
        query = f"""
                mutation ($file: File!) {{
                    add_file_to_update(update_id: "{update_id}", file: $file) {{
                        id
                    }}
                }}
            """

        return await self.client_file_upload.execute(query, variables={"file": file})
