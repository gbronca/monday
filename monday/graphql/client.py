"""Provide a GraphQL client to connect to Monday.com's GraphQL API."""

import json

import httpx
from anyio import open_file

from monday.exceptions import MondayError


class GraphQLClient:
    """GraphQL Client to connect to Monday GraphQL API."""

    def __init__(
        self: "GraphQLClient",
        endpoint: str,
        api_key: str | None = None,
        api_version: str | None = None,
    ) -> None:
        """Initialize a new instance of GraphQLClient."""
        self.endpoint = endpoint
        self.api_key = api_key
        self.api_version = api_version

    async def execute(
        self: "GraphQLClient",
        query: str,
        variables: dict | None = None,
    ) -> dict:
        """Execute a GraphQL query.

        Args:
            query (str): The GraphQL query string to execute.
            variables (str | None, optional): The variables to pass to the query.
                Defaults to None.

        Returns:
            dict: The response from the GraphQL API.
        """
        return await self._execute(query, variables)

    async def _execute(
        self: "GraphQLClient",
        query: str,
        variables: dict | None = None,
    ) -> dict:
        payload = {"query": query}
        headers = {}
        files = None

        if self.api_key:
            headers["Authorization"] = self.api_key

        if self.api_version:
            headers["API-Version"] = self.api_version

        if variables is None:
            headers.setdefault("Content-Type", "application/json")
            payload = json.dumps({"query": query}).encode("utf-8")  # type: ignore

        elif variables.get("file", None) is not None:
            headers.setdefault("content", "multipart/form-data")
            async with await open_file(variables["file"], "rb") as var_file:
                contents = await var_file.read()
            files = [("variables[file]", (variables["file"], contents))]

        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    url=self.endpoint,
                    headers=headers,
                    data=payload,
                    files=files,
                    timeout=120,
                )
            response.raise_for_status()
            if "errors" in response.json():
                json_errors = response.json()["errors"][0]
                raise (
                    MondayError(json_errors["message"])
                    if "message" in json_errors
                    else MondayError(json_errors)
                )
            if "error_message" in response.json():
                raise MondayError(response.json()["error_message"])
            return response.json()
        except (httpx.HTTPError, json.JSONDecodeError, MondayError) as error:
            raise error
