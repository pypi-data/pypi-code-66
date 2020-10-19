"""

Copyright (c) 2020, Vanessa Sochat

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""
from rest_framework.authtoken.models import Token


def get_usertoken(user):
    try:
        token = Token.objects.get(user=user)
    except Token.DoesNotExist:
        token = Token.objects.create(user=user)
    return token.key


def get_token(request):
    """The same as validate_token, but return the token object to check the
    associated user.
    """
    # Coming from HTTP, look for authorization as bearer token
    token = request.META.get("HTTP_AUTHORIZATION")

    if token:
        try:
            return Token.objects.get(key=token.replace("BEARER", "").strip())
        except Token.DoesNotExist:
            pass

    # Next attempt - try to get token via user session
    elif request.user.is_authenticated and not request.user.is_anonymous:
        try:
            return Token.objects.get(user=request.user)
        except Token.DoesNotExist:
            pass


def get_challenge(repository, scopes=["pull", "push"]):
    """Given an unauthenticated request, return a challenge in
    the Www-Authenticate header
    """
    if not isinstance(scopes, list):
        scopes = [scopes]
    return 'realm="%s/auth/token",service="%s",scope="repository:%s:%s"' % (
        settings.DOMAIN_NAME,
        settings.DOMAIN_NAME,
        repository,
        ",".join(scopes),
    )
