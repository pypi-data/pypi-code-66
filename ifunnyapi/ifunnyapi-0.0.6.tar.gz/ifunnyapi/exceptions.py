class iFunnyAPIException(Exception):
    """Base exception class"""


class APIError(iFunnyAPIException):
    """Raised when an API request retrieves an error"""

    def __init__(self, status: int, desc: str):
        self.status = status
        self.desc = desc

    def __str__(self):
        return f"status {self.status}, {self.desc}"
