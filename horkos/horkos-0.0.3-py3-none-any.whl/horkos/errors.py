class Error(Exception):
    """Base error."""


class SchemaValidationError(Error):
    """The given data schema failed to validate."""
