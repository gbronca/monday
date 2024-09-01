"""Class for interacting with the Monday.com API's Users endpoint."""

from monday.resources.base import BaseResource
from monday.resources.types.types import UserKind
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
