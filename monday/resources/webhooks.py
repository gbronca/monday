"""This module provides the Webhooks class for querying webhooks."""

from monday.resources.base import BaseResource


class WebhookResource(BaseResource):
    """Represents a resource for querying webhooks."""

    async def fetch_webhooks(
        self: "WebhookResource",
        board_id: str,
        app_webhooks_only: bool | None = None,
    ) -> dict:
        """This method allows you to query webhooks.

        Querying webhooks will return one or a collection of webhooks.
        You can only query webhooks directly at the root, so it can't be nested
        within another query.

        Args:
            board_id (str): The unique identifier of the board that your webhook
                subscribes to.
            app_webhooks_only (bool): Returns only the webhooks created by the app
                initiating the request.

        Returns:
            dict: Dict response from the monday.com GraphQL API
        """
        query = f"""query {{
            webhooks(board_id: {board_id}
            {f", app_webhooks_only: {app_webhooks_only}" if app_webhooks_only else ""}
            ) {{
                id
                event
                board_id
                config
            }}
        }}"""

        return await self.client.execute(query)

    async def delete_webhook(
        self: "WebhookResource",
        webhook_id: str,
    ) -> dict:
        """This method allows you to delete a webhook.

        After the mutation runs, it will no longer report events to the URL given.

        Args:
            webhook_id (str): The webhook's unique identifier.

        Returns:
            dict: Dict response from the monday.com GraphQL API
        """
        query = f"""mutation {{
            delete_webhook (id: {webhook_id}) {{
                id
                board_id
            }}
        }}"""

        return await self.client.execute(query)
