import json


def monday_json_stringify(value):
    """Converts a python object to a JSON string that can be used in a monday.com query

    Args:
        value (object): Monday query string

    Returns:
        json: JSON string
    """

    # Monday's API requires a JSON encoded string for JSON values. json.dumps and
    # JSON.stringify don't really work for this.
    # The only thing that works is a JSON encoded, JSON encoded string.

    return json.dumps(json.dumps(value))
