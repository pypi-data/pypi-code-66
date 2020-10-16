import os
from magicapi.Errors.MagicExceptions import (
    MagicException,
    BackendException,
    FrontendException,
    FirestoreException,
    TwilioException,
)

os.environ["DEFAULT_EXCEPTION"] = BackendException

print(os.getenv("DEFAULT_EXCEPTION"))
