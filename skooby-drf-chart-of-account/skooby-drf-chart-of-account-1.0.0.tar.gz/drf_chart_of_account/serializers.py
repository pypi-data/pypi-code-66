"""Chart of Accounts Models Serializers Classes."""
from rest_framework import serializers
from .models import (LayersBaseModel, LayerOneModel, LayerTwoModel,
                     LayerThreeModel, LayerFourModel, LayerFiveModel)


class LayersModelBaseSerializer(serializers.ModelSerializer):
    """The base serializer class for all the layers model.

    All other serializer class with extend this base model.
    """

    class Meta:
        """Meta data class for the base serializer."""

        model = LayersBaseModel
        fields = '__all__'
        read_only_fields = ['id', 'ref_no', 'layer_no', 'created_at', 'updated_at']

    def update(self, instance, validated_data):
        """Update the instance with custom update validation checking."""
        if instance.validate_update():
            return super(LayersModelBaseSerializer, self).update(instance, validated_data)


class LayerOneModelSerializer(LayersModelBaseSerializer):
    """LayerOneModel class serializer."""

    class Meta(LayersModelBaseSerializer.Meta):
        """Meta data class for the LayerOneModelSerializer."""

        model = LayerOneModel


class LayerTwoModelSerializer(LayersModelBaseSerializer):
    """LayerTwoModel class serializer."""

    class Meta(LayersModelBaseSerializer.Meta):
        """Meta data class for the LayerTwoModelSerializer."""

        model = LayerTwoModel


class LayerThreeModelSerializer(LayersModelBaseSerializer):
    """LayerThreeModel class serializer."""

    class Meta(LayersModelBaseSerializer.Meta):
        """Meta data class for the LayerThreeModelSerializer."""

        model = LayerThreeModel


class LayerFourModelSerializer(LayersModelBaseSerializer):
    """LayerFourModel class serializer."""

    class Meta(LayersModelBaseSerializer.Meta):
        """Meta data class for the LayerFourModelSerializer."""

        model = LayerFourModel


class LayerFiveModelSerializer(LayersModelBaseSerializer):
    """LayerFiveModel class serializer."""

    class Meta(LayersModelBaseSerializer.Meta):
        """Meta data class for the LayerFiveModelSerializer."""

        model = LayerFiveModel
