"""This module provides the Workspace class for querying workspaces."""

import json
from typing import Literal, Unpack

from monday.resources.base import BaseResource
from monday.resources.types.workspaces import Workspace


class WorkspaceResource(BaseResource):
    """Represents a resource for querying workspaces."""

    def fetch_workspaces(
        self: "WorkspaceResource",
        **kwargs: Unpack[Workspace],
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
        if kwargs:
            keys_to_not_dump = {"kind", "state", "order_by"}
            arguments = [
                f"{key}: {value if key in keys_to_not_dump else json.dumps(value)}"
                for key, value in kwargs.items()
            ]

        query = """query
        {
            workspaces %s {
                id
                name
                kind
                account_product {
                    id
                }
                description
                created_at
                owners_subscribers {
                    id
                    name
                    email
                }
                state
                teams_subscribers {
                    id
                    name
                }
                users_subscribers {
                    id
                    name
                    email
                }
            }
        }""" % (f"({", ".join(arguments)})" if arguments else "")

        return self.client.execute(query)

    def create_workspace(
        self: "WorkspaceResource",
        name: str,
        kind: Literal["open", "closed"],
        description: str = "",
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
                description: "{description}"
                ) {{
                id
                name
                kind
                description
            }}
        }}"""

        return self.client.execute(query)

    def update_workspace(
        self: "WorkspaceResource",
        workspace_id: str,
        attributes: str,
    ) -> dict:
        """Update a workspace via the API.

        Args:
            workspace_id (str): The identifier of the workspace to update.
            attributes (str): The attribute to update in the workspace as a json string.
                allowed keys: name, description, kind
                e.g. {name:"Marketing team", description: "Marketing team workspace"}

        Returns:
            dict: The updated workspace information.
        """
        query = f"""mutation {{
            update_workspace (
                id: "{workspace_id}",
                attributes: {attributes}
            ) {{
                id
                name
                kind
                description
            }}
        }}"""

        return self.client.execute(query)

    def delete_workspace(self: "WorkspaceResource", workspace_id: str) -> dict:
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

        return self.client.execute(query)

    def add_users_to_workspace(
        self: "WorkspaceResource",
        workspace_id: str,
        user_ids: list[str] | str,
        kind: Literal["subscriber", "owner"] = "subscriber",
    ) -> dict:
        """Allows you to add users to a workspace via the API.

        You can specify which users to add to the workspace and their subscription type.

        Args:
            workspace_id (str): The workspace's unique identifier.
            user_ids (str | [str]): The ID's of the users to add to the workspace.
            kind (str): Kind of subscribers added: subscriber or owner.

        Returns:
            dict: dict response from the monday.com GraphQL API
        """
        if not isinstance(user_ids, list):
            user_ids = [str(user_ids)]

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

        return self.client.execute(query)

    def delete_users_from_workspace(
        self: "WorkspaceResource",
        workspace_id: str,
        user_ids: list[str] | str,
    ) -> dict:
        """Allows you to delete users from a workspace via the API.

        Args:
            workspace_id (str): The workspace's unique identifier.
            user_ids (str | [str]): The IDs of the users to remove from the workspace.

        Returns:
            dict: dict response from the monday.com GraphQL API
        """
        if not isinstance(user_ids, list):
            user_ids = [str(user_ids)]

        query = f"""mutation
        {{
            delete_users_from_workspace (
                workspace_id: "{workspace_id}",
                user_ids: {json.dumps(user_ids)}
            ) {{
                id
            }}
        }}"""

        return self.client.execute(query)

    def add_teams_to_workspace(
        self: "WorkspaceResource",
        workspace_id: str,
        team_ids: list[str] | str,
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
        if not isinstance(team_ids, list):
            team_ids = [str(team_ids)]

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

        return self.client.execute(query)

    def delete_teams_from_workspace(
        self: "WorkspaceResource",
        workspace_id: str,
        team_ids: list[str] | str,
    ) -> dict:
        """Allows you to delete teams from a workspace via the API.

        Args:
            workspace_id (str): The workspace's unique identifier.
            team_ids (str | [str]): The ID's of the teams to remove from the workspace.

        Returns:
            dict: dict response from the monday.com GraphQL API
        """
        if not isinstance(team_ids, list):
            team_ids = [str(team_ids)]

        query = f"""mutation
        {{
            delete_teams_from_workspace (
                workspace_id: "{workspace_id}",
                team_ids: {json.dumps(team_ids)}
            ) {{
                id
            }}
        }}"""

        return self.client.execute(query)
