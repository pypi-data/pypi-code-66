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

from django.conf import settings
from django.urls import reverse

from django_oci.models import Repository, Image
from .permissions import IsStaffOrSuperUser, AllowAnyGet
from rest_framework import generics, mixins, serializers, viewsets, status
from rest_framework.exceptions import PermissionDenied, NotFound

from rest_framework.response import Response
from rest_framework.views import APIView

# Repository


class RepositorySerializer(serializers.ModelSerializer):
    def get_label(self, instance):
        return instance.get_label()

    class Meta:
        model = Repository
        fields = ("uuid", "name", "email", "affiliation", "orcid", "tags", "label")


class RepositoryViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Repository.objects.all()

    serializer_class = RepositorySerializer
    permission_classes = (AllowAnyGet,)


# Image


class ImageSerializer(serializers.ModelSerializer):

    plates = serializers.SerializerMethodField("plates_list")
    parent = serializers.PrimaryKeyRelatedField(queryset=Image.objects.all())
    label = serializers.SerializerMethodField("get_label")

    def plates_list(self, container):
        return [
            {"name": plate.name, "uuid": plate.uuid}
            for plate in container.plate_set.all()
        ]

    def get_label(self, container):
        return container.get_label()

    class Meta:
        model = Image
        fields = (
            "uuid",
            "time_created",
            "time_updated",
            "name",
            "container_type",
            "description",
            "estimated_temperature",
            "x",
            "y",
            "z",
            "parent",
            "plates",
            "label",
        )


class ImageViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Image.objects.all()

    serializer_class = ImageSerializer
    permission_classes = (IsStaffOrSuperUser,)
