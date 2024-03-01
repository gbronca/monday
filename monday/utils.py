"""Provides utility functions for Monday.com API."""
import json


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
