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

from django.conf.urls import url, include
import rest_framework.authtoken.views as authviews
from rest_framework import routers
from django_oci import settings
from .serializers import RepositoryViewSet, ImageViewSet

router = routers.DefaultRouter()
router.register(r"^repositories", RepositoryViewSet, basename="repository")
router.register(r"^images", ImageViewSet, basename="image")

urlpatterns = [
    url(r"^" + settings.URL_PREFIX + "/", include(router.urls)),
    url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    url(r"^api-token-auth/", authviews.obtain_auth_token),
]
