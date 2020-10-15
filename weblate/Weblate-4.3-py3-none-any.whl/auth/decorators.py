#
# Copyright © 2012 - 2020 Michal Čihař <michal@cihar.com>
#
# This file is part of Weblate <https://weblate.org/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#


from functools import wraps

from django.core.exceptions import PermissionDenied


def management_access(view):
    """Decorator that checks management access."""

    @wraps(view)
    def wrapper(request, *args, **kwargs):
        if not request.user.has_perm("management.use"):
            raise PermissionDenied
        return view(request, *args, **kwargs)

    return wrapper
