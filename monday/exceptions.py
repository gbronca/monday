"""Exceptions for the Monday.com API client."""


class ArgumentError(Exception):
    """Raised when a function argument is invalid or missing."""

    pass


class MondayError(Exception):
    """Raised when a function argument is invalid or missing."""

    pass


class MondayQueryError(MondayError):
    """Raised when a query to Monday API fails."""

    def __init__(
        self: "MondayQueryError",
        message: str,
        query: str,
        variables: dict | None = None,
    ) -> None:
        """Initialize a new instance of MondayQueryError."""
        self.query = query
        self.variables = variables
        super().__init__(message)
