from rest_framework.viewsets import ModelViewSet

from netbox_pseudo_wire.models import Pseudowire
from .serializers import PseudowireSerializer


class PseudowireViewSet(ModelViewSet):
    queryset = Pseudowire.objects.all()
    serializer_class = PseudowireSerializer
