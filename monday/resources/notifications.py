"""This module contains the NotificationResource class for handling notifications."""

from typing import Literal

from monday.resources.base import BaseResource


class NotificationResource(BaseResource):
    """Class representing a notification resource."""

    def create_notification(
        self: "NotificationResource",
        user_id: str,
        target_id: str,
        text: str,
        target_type: Literal["project", "post"],
    ) -> dict:
        """Allows you to send a notification to the bell icon via the API.

        Doing so may also send an email if the recipient's email preferences
        are set up accordingly. Please note that this mutation only sends the
        notification; you can't query back the notification ID when running
        the mutation, as notifications are asynchronous.

        If you send a notification from a board view or widget using seamless
        authentication, it will come from the app and display its name and icon.
        If you use a personal API key to make the call, the notification will
        appear to come from the user who installed the app on the account.

        user_id (str): The user's unique identifier.
        target_id (str): The target's identifier.
        text (str): The notification text.
        target_type (Literal["project", "post"]): The target's type: project / post.
            - Project: sends a notification referring to a specific item or board
            - Post : sends a notification referring to a specific item's update or
            reply

        Returns:
            (dict): dictionary response from the API
        """
        query = f"""mutation {{
            create_notification (
                user_id: "{user_id}",
                target_id: "{target_id}",
                text: "{text}",
                target_type: {target_type}
            ) {{
                text
            }}
        }}"""

        return self.client.execute(query)
