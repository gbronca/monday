"""This module provides the Workspace class for querying workspaces."""

import json
from typing import Literal, TypedDict, Unpack

from monday.resources.base import BaseResource


class Workspace(TypedDict, total=False):
    """Represents a workspace with optional attributes."""

    ids: list[str] | str
    kind: Literal["open", "closed"]
    limit: int
    state: Literal["all", "active", "archived", "deleted"]
    order_by: Literal["created_at"]
    page: int


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
        query = """mutation {
            create_workspace (
                name: "%(name)s",
                kind: %(kind)s,
                description: "%(description)s"
                ) {
                id
                name
                kind
                description
            }
        }""" % {"name": name, "kind": kind, "description": description}  # noqa: UP031

        return self.client.execute(query)

    def delete_workspace(self: "WorkspaceResource", workspace_id: str) -> dict:
        """Allows you to delete a workspace.

        Args:
            workspace_id (str): The workspace's identifier.

        Returns:
            dict: dict response from the monday.com GraphQL API
        """
        query = """mutation {
            delete_workspace ( workspace_id: "%(id)s") {
                id
            }
        }""" % {"id": workspace_id}  # noqa: UP031

        return self.client.execute(query)
