"""Class for interacting with the Monday.com API's Users endpoint."""

from monday.resources.base import BaseResource
from monday.resources.types.types import BoardSubscriberKind, UserKind
from monday.utils import parse_parameters


class UserResource(BaseResource):
    """Class for interacting with the Monday.com API's Users endpoint."""

    async def fetch_users(
        self: "UserResource",
        emails: list[str] | str | None = None,
        ids: list[str] | str | None = None,
        kind: UserKind | None = None,
        limit: int | None = None,
        name: str | None = None,
        page: int | None = None,
        *,
        newest_first: bool | None = None,
        non_active: bool | None = None,
    ) -> dict:
        """Fetch user(s) data from Monday.com.

        Every user in monday.com is a part of an account (i.e an organization) and
        could be a member or a guest in that account.

        Querying users returns one or multiple users.

        Kwargs:
            emails ([str] | str): A list of users' emails.
            ids ([str] | str): A list of users' unique identifiers.
            kind (str): The kind of users you want to search by:
                all, non_guests, guests, non_pending.
            limit (int): Number of users to get.
            name (str): A fuzzy search of users by name.
            newest_first (bool): Get the recently created users at the top of the list.
            non-active (bool): Returns the account's non-active users.
            page (int): The page number to return. Starts at 1.

        Returns:
            dict: dict response from the monday.com GraphQL API
        """
        parameters = parse_parameters(locals(), literals=["kind"])

        query = f"""query
        {{
            users {f"({", ".join(parameters)})" if parameters else ""} {{
                id
                birthday
                country_code
                created_at
                current_language
                email
                enabled
                is_admin
                is_guest
                is_pending
                is_verified
                is_view_only
                join_date
                last_activity
                location
                mobile_phone
                name
                out_of_office {{
                    active
                    disable_notifications
                    end_date
                    start_date
                    type
                }}
                phone
                photo_original
                photo_small
                teams {{
                    id
                    name
                }}
                time_zone_identifier
                title
                url
                utc_hours_diff
            }}
        }}"""

        return await self.client.execute(query)

    async def fetch_current_user(self: "UserResource") -> dict:
        """Returns the user details of the user whose API key is being used.

        Returns:
            dict: dict response from the monday.com GraphQL API
        """
        query = """
            query {
                me {
                    birthday
                    country_code
                    created_at
                    join_date
                    email
                    enabled
                    id
                    is_admin
                    is_guest
                    is_pending
                    is_view_only
                    location
                    mobile_phone
                    name
                    phone
                    photo_original
                    photo_small
                    teams {
                        id
                        name
                    }
                    time_zone_identifier
                    title
                    url
                    utc_hours_diff
                }
            }
        """

        return await self.client.execute(query)

    async def add_users_to_board(
        self: "UserResource",
        board_id: str,
        user_ids: list[str] | str,
        kind: BoardSubscriberKind | None = None,
    ) -> dict:
        """Allows you to add users to a board.

        Args:
            board_id (str): The board's unique identifier.
            user_ids ([str]): List of user ids to subscribe to the board.
            kind (str): Subscribers kind: subscriber or owner. Default is 'owner'

        Returns:
            dict: dictionary response from the monday.com GraphQL API
        """
        parameters = parse_parameters(locals(), literals=["kind"])

        query = f"""mutation {{
            add_users_to_board ({", ".join(parameters)}) {{
                id
            }}
        }}"""

        return await self.client.execute(query)

    async def delete_subscribers_from_board(
        self: "UserResource",
        board_id: str,
        user_ids: list[str] | str,
    ) -> dict:
        """Allows you to delete subscribers from a board.

        board_id (str): The board's unique identifier.
        user_ids ([str]): List of user ids to unsubscribe from the board.

        Returns:
            dict: dictionary response from the monday.com GraphQL API
        """
        parameters = parse_parameters(locals())

        query = f"""mutation {{
            delete_subscribers_from_board ({", ".join(parameters)}) {{
                id
            }}
        }}"""

        return await self.client.execute(query)
