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

from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsStaffOrSuperUser(BasePermission):
    """Allows access to staff (admin) or superuser."""

    def has_permission(self, request, view):

        if request.user.is_staff or request.user.is_superuser:
            return True

        return request.method in SAFE_METHODS


class AllowAnyGet(BasePermission):
    """Allows an anonymous user access for GET requests only."""

    def has_permission(self, request, view):

        if request.user.is_anonymous and request.method == "GET":
            return True

        if request.user.is_staff or request.user.is_superuser:
            return True

        return request.method in SAFE_METHODS
