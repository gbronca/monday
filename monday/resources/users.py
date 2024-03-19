"""Class for interacting with the Monday.com API's Users endpoint."""

import json
from typing import TypedDict

from monday.resources.base import BaseResource


class Users(TypedDict):
    """Type definition for users."""

    id: list | str
    emails: list | str
    kind: str
    limit: int
    name: str
    newest_first: bool
    non_active: bool
    page: int


class UserResource(BaseResource):
    """Class for interacting with the Monday.com API's Users endpoint."""

    def fetch_users(self: "UserResource", **kwargs: Users) -> dict:
        """Fetch user(s) data from Monday.com.

        Every user in monday.com is a part of an account (i.e an organization) and
        could be a member or a guest in that account.

        Querying users returns one or multiple users.

        Kwargs:
            ids ([str]): A list of users' unique identifiers.
            kind (str): The kind of users you want to search by:
                all,
                non_guests,
                guests,
                non_pending.
            newest_first (bool): Get the recently created users at the top of the list.
            limit (int): Number of users to get.
            emails ([str]): A list of users' emails.
            page (int): The page number to return. Starts at 1.
            name (str): A fuzzy search of users by name.

        Returns:
            dict: dict response from the monday.com GraphQL API
        """
        query = """query
        {
            users (%s) {
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
                out_of_office {
                    active
                    disable_notifications
                    end_date
                    start_date
                    type
                }
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
        }""" % ", ".join(
            [
                f"{arg}: {json.dumps(kwargs.get(arg))}"
                if arg != "newest_first"
                else f"{arg}: {str(kwargs.get(arg)).lower()}"
                for arg in kwargs
            ],
        )

        return self.client.execute(query)

    def fetch_current_user(self: "UserResource") -> dict:
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

        return self.client.execute(query)
