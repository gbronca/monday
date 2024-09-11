"""This module provides the Folder class for accessing the Teams endpoint."""

from monday.resources.base import BaseResource
from monday.utils import parse_parameters

from .types.types import FolderColor


class FolderResource(BaseResource):
    """Class for interacting with the Monday.com API's Folder endpoint."""

    async def fetch_folders(
        self: "FolderResource",
        ids: list[str] | str | None = None,
        limit: int = 25,
        page: int = 1,
        workspace_ids: list[str] | str | None = None,
    ) -> dict:
        """Querying folders will return metadata about one or a collection of folders.

        Args:
            ids (str | [str], optional): The specific folders to return.
            limit (int): The number of folders to get.
                The default is 25 and the maximum is 100.
            page (int): The page number to return. Starts at 1.
            workspace_ids (str | [str], optional): The unique identifiers of
                the specific workspaces to return.

        Returns:
            dict: dictionary response from the monday.com GraphQL API
        """
        parameters = parse_parameters(locals())

        query = f"""
            query {{
                folders {f"({", ".join(parameters)})" if parameters else ""} {{
                    id
                    name
                    owner_id
                    color
                    created_at
                    children {{
                        id
                        name
                    }}
                    workspace {{
                        id
                        name
                    }}
                    parent {{
                        id
                        name
                    }}
                    sub_folders {{
                        id
                        name
                    }}
                }}
            }}
        """

        return await self.client.execute(query)

    async def create_folder(
        self: "FolderResource",
        name: str,
        workspace_id: str,
        color: FolderColor | None = None,
        parent_folder_id: str | None = None,
    ) -> dict:
        """Allows you to create a new folder in aworkspace via the API.

        Args:
            name (str): The folder's name.
            workspace_id (str): The unique identifier of the workspace to create
                the new folder in.
            color (str, optional): The folder's color. Defaults to None.
            parent_folder_id (str, optional): The ID of the folder you want to nest the
                new one under. Defaults to None.

        Returns:
            dict: Dictionary response from the monday.com GraphQL API
        """
        parameters = parse_parameters(locals())
        query = f"""mutation {{
            create_folder ({", ".join(parameters)}) {{
                id
                name
            }}
        }}"""

        return await self.client.execute(query)
