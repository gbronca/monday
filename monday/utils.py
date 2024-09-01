"""Provides utility functions for Monday.com API."""

import json
from typing import Any


def monday_json_stringify(value: object) -> str:
    """Convert a python object to a compatible JSON string.

    Args:
        value (oject): Monday query string

    Returns:
        json: JSON string

    """
    # Monday's API requires a JSON encoded string for JSON values. json.dumps() doesn't
    # work. The only thing that works is a JSON encoded, JSON encoded string.

    return json.dumps(json.dumps(value))


def parse_parameters(
    parameters: dict[str, Any],
    literals: list[str] | None = None,
    exclude: list[str] | None = None,
) -> list[str]:
    """Parse parameters for a query.

    Args:
        parameters (dict): The parameters to parse.
        literals (list, optional): The literal values. Defaults to None.
        exclude (list, optional): The keys to exclude. Defaults to None.

    Returns:
        list: The parsed parameters.
    """
    parameters.pop("self", None)
    parameters.pop("all_fields", None)
    if exclude:
        for key in exclude:
            parameters.pop(key, None)
    if literals:
        return [
            f"{key}: {value if key in literals else json.dumps(value)}"
            for key, value in parameters.items()
            if value is not None
        ]
    else:
        return [
            f"{key}: {json.dumps(value)}"
            for key, value in parameters.items()
            if value is not None
        ]
