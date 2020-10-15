# coding: utf-8

# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.pet_api import PetApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from passbase_sdk.api.identity_api import IdentityApi
from passbase_sdk.api.project_api import ProjectApi
from passbase_sdk.api.user_api import UserApi
