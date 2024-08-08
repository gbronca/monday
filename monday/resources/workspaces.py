"""This module provides the Workspace class for querying workspaces."""

import json
from typing import Literal

from monday.resources.base import BaseResource
from monday.utils import parse_parameters


class WorkspaceResource(BaseResource):
    """Represents a resource for querying workspaces."""

    async def fetch_workspaces(
        self: "WorkspaceResource",
        ids: str | list[str] | None = None,
        kind: Literal["open", "closed"] | None = None,
        limit: int | None = None,
        order_by: Literal["created_at"] | None = None,
        page: int | None = None,
        state: Literal["active", "all", "archived", "deleted"] | None = None,
    ) -> dict:
        """This method allows you to query workspaces.

        It can return one or a collection of workspaces.

        Kwargs:
            ids (str | [str]): The workspace's identifier.
            kind (str): The workspace's kind: open or closed.
            limit (int): The number of items returned. The default is 25.
            state (str): The state of the workspace: all, active, archived, or deleted.
                The default is active.
            order_by (str): The order in which to retrieve your boards.
                For now, you can only order by created_at.
            page (int): The page number to get, starting at 1.

        Returns:
            (dict): Dict response from the monday.com GraphQL API
        """
        parameters = parse_parameters(locals(), exclude=["kind", "state", "order_by"])
        query = f"""query
        {{
            workspaces {f"({", ".join(parameters)})" if parameters else ""} {{
                id
                name
                account_product {{
                    id
                    kind
                }}
                created_at
                description
                is_default_workspace
                kind
                owners_subscribers {{
                    id
                    name
                    email
                }}
                state
                team_owners_subscribers {{
                    id
                    name
                    picture_url
                }}
                teams_subscribers {{
                    id
                    name
                    picture_url
                }}
                users_subscribers {{
                    id
                    name
                    email
                }}
            }}
        }}"""

        return await self.client.execute(query)

    async def create_workspace(
        self: "WorkspaceResource",
        name: str,
        kind: Literal["open", "closed"],
        description: str | None = None,
    ) -> dict:
        """Allows you to create a new workspace.

        After the mutation runs, you can create boards in the workspace.

        Args:
            name (str): The new workspace's name.
            kind (str): The new workspace's kind: open or closed.
            description (str, optional): The new workspace's description.

        Returns:
            dict: dict response from the monday.com GraphQL API
        """
        query = f"""mutation {{
            create_workspace (
                name: "{name}",
                kind: {kind},
                {f'description: "{description}"' if description else ""}
                ) {{
                id
                name
                kind
                description
            }}
        }}"""
        return await self.client.execute(query)

    async def update_workspace(
        self: "WorkspaceResource",
        workspace_id: str,
        name: str | None = None,
        description: str | None = None,
        kind: Literal["open", "closed"] | None = None,
    ) -> dict:
        """Update a workspace via the API.

        Args:
            workspace_id (str): The identifier of the workspace to update.
            name (str, optional): The new name of the workspace.
            description (str, optional): The new description of the workspace.
            kind (str, optional): The new kind of the workspace.

        Returns:
            dict: The updated workspace information.
        """
        attributes: list[str] = []
        if name:
            attributes.append(f"name: {json.dumps(name)}")
        if description:
            attributes.append(f"description: {json.dumps(description)}")
        if kind:
            attributes.append(f"kind: {kind}")

        query = f"""mutation {{
            update_workspace (
                id: "{workspace_id}",
                attributes: {{{", ".join(attributes)}}}
            ) {{
                id
                name
                kind
                description
            }}
        }}"""
        return await self.client.execute(query)

    async def delete_workspace(self: "WorkspaceResource", workspace_id: str) -> dict:
        """Allows you to delete a workspace.

        Args:
            workspace_id (str): The workspace's identifier.

        Returns:
            dict: dict response from the monday.com GraphQL API
        """
        query = f"""mutation {{
            delete_workspace ( workspace_id: "{workspace_id}") {{
                id
            }}
        }}"""

        return await self.client.execute(query)

    async def add_users_to_workspace(
        self: "WorkspaceResource",
        workspace_id: str,
        user_ids: list[str],
        kind: Literal["subscriber", "owner"] = "subscriber",
    ) -> dict:
        """Allows you to add users to a workspace via the API.

        You can specify which users to add to the workspace and their subscription type.

        Args:
            workspace_id (str): The workspace's unique identifier.
            user_ids ([str]): The ID's of the users to add to the workspace.
            kind (str): Kind of subscribers added: subscriber or owner.

        Returns:
            dict: dict response from the monday.com GraphQL API
        """
        query = f"""mutation
        {{
            add_users_to_workspace (
                workspace_id: "{workspace_id}",
                user_ids: {json.dumps(user_ids)},
                kind: {kind}
            ) {{
                id
            }}
        }}"""

        return await self.client.execute(query)

    async def delete_users_from_workspace(
        self: "WorkspaceResource",
        workspace_id: str,
        user_ids: list[str],
    ) -> dict:
        """Allows you to delete users from a workspace via the API.

        Args:
            workspace_id (str): The workspace's unique identifier.
            user_ids ([str]): The IDs of the users to remove from the workspace.

        Returns:
            dict: dict response from the monday.com GraphQL API
        """
        query = f"""mutation
        {{
            delete_users_from_workspace (
                workspace_id: "{workspace_id}",
                user_ids: {json.dumps(user_ids)}
            ) {{
                id
            }}
        }}"""

        return await self.client.execute(query)

    async def add_teams_to_workspace(
        self: "WorkspaceResource",
        workspace_id: str,
        team_ids: list[str],
        kind: Literal["subscriber", "owner"] = "subscriber",
    ) -> dict:
        """Allows you to add teams to a workspace via the API.

        Args:
            workspace_id (str): The workspace's unique identifier.
            team_ids (str | [str]): The ID's of the teams to add to the workspace.
            kind (str): Kind of subscribers added: subscriber or owner.

        Returns:
            dict: dict response from the monday.com GraphQL API
        """
        query = f"""mutation
        {{
            add_teams_to_workspace (
                workspace_id: "{workspace_id}",
                team_ids: {json.dumps(team_ids)},
                kind: {kind}
            ) {{
                id
            }}
        }}"""

        return await self.client.execute(query)

    async def delete_teams_from_workspace(
        self: "WorkspaceResource",
        workspace_id: str,
        team_ids: list[str],
    ) -> dict:
        """Allows you to delete teams from a workspace via the API.

        Args:
            workspace_id (str): The workspace's unique identifier.
            team_ids (str | [str]): The ID's of the teams to remove from the workspace.

        Returns:
            dict: dict response from the monday.com GraphQL API
        """
        query = f"""mutation
        {{
            delete_teams_from_workspace (
                workspace_id: "{workspace_id}",
                team_ids: {json.dumps(team_ids)}
            ) {{
                id
            }}
        }}"""

        return await self.client.execute(query)
