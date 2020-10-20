from rest_framework.serializers import ModelSerializer
from netbox_pseudo_wire.models import Pseudowire


class PseudowireSerializer(ModelSerializer):
    class Meta:
        model = Pseudowire
        fields = ("id", "name", "tunnel")
