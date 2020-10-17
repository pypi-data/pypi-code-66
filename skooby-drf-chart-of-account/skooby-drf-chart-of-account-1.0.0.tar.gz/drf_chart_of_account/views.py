"""Chart of Accounts View Classes."""
from rest_framework import viewsets
from .serializers import (LayerOneModelSerializer, LayerTwoModelSerializer,
                          LayerThreeModelSerializer, LayerFourModelSerializer,
                          LayerFiveModelSerializer)


# Create your views here.
class LayerOneModelViewSet(viewsets.ModelViewSet):
    """A simple ViewSet for viewing and editing layers."""

    serializer_class = LayerOneModelSerializer
    queryset = serializer_class.Meta.model.objects.filter(is_active=True)


class LayerTwoModelViewSet(viewsets.ModelViewSet):
    """A simple ViewSet for viewing and editing layers."""

    serializer_class = LayerTwoModelSerializer
    queryset = serializer_class.Meta.model.objects.filter(is_active=True)


class LayerThreeModelViewSet(viewsets.ModelViewSet):
    """A simple ViewSet for viewing and editing layers."""

    serializer_class = LayerThreeModelSerializer
    queryset = serializer_class.Meta.model.objects.filter(is_active=True)


class LayerFourModelViewSet(viewsets.ModelViewSet):
    """A simple ViewSet for viewing and editing layers."""

    serializer_class = LayerFourModelSerializer
    queryset = serializer_class.Meta.model.objects.filter(is_active=True)


class LayerFiveModelViewSet(viewsets.ModelViewSet):
    """A simple ViewSet for viewing and editing layers."""

    serializer_class = LayerFiveModelSerializer
    queryset = serializer_class.Meta.model.objects.filter(is_active=True)
