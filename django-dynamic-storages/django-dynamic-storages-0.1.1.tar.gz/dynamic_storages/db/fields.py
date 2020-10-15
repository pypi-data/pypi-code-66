import logging
from django.db.models.fields.files import FieldFile, FileField, ImageField
from django.core.files.images import ImageFile

import json
from fernet_fields import EncryptedTextField
from django.core.serializers.json import DjangoJSONEncoder

log = logging.getLogger(__name__)

class FileFieldMixin(object):
    def pre_save(self, model_instance, add):
        if getattr(self, '_storage_callable', None):
            if callable(self._storage_callable):
                self.storage = self._storage_callable(model_instance)
        return super().pre_save(model_instance, add)


class EncryptedJSONField(EncryptedTextField):
    """JSON dictionary that is encrypted at rest as a text object - based off of the django-fernet-fields EncryptedTextField"""
    def get_prep_value(self, value):
        ret_val = "{}"
        if value:
            ret_val = json.dumps(value, separators=(",", ":"), cls=DjangoJSONEncoder)
        return ret_val

    def to_python(self, value):
        ret_val = {}
        if isinstance(value, dict):
            ret_val = value
        elif isinstance(value, str):
            ret_val = json.loads(value)
        return ret_val

class DynamicStorageFieldFile(FieldFile):
    """FieldFile implementation for dynamically setting the storage provider for the file at runtime based on a callable passed into the field definition"""
    def __init__(self, instance, field, name):
        if getattr(field, '_storage_callable', None):
            storage = field._storage_callable(instance)
            log.info('Setting storage for this field to {}'.format(storage))
            field.storage = storage
        super().__init__(instance, field, name)


class DynamicStorageFileField(FileFieldMixin, FileField):
    """File field implementation for dynamically setting the storage provider for the file to be stored/retrieved at runtime based on a callable passed into this field definition for the `storage` kwarg"""
    attr_class = DynamicStorageFieldFile


class DynamicStorageImageFieldFile(ImageFile, DynamicStorageFieldFile):
    def delete(self, save=True):
        # Clear the image dimensions cache
        if hasattr(self, '_dimensions_cache'):
            del self._dimensions_cache
        super().delete(save)

class DynamicStorageImageField(FileFieldMixin, ImageField):
    """Image field implementation for dynamically setting the storage provider for the image to be stored/retrieved at runtime based on a callable passed into this field definition for the `storage` kwarg"""
    attr_class = DynamicStorageImageFieldFile
