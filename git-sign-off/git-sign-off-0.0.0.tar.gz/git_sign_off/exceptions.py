class GitError(Exception):
    """
    Signals a git issue.
    """


class SignatureError(ValueError):
    """
    Signals an invalid signature.
    """
