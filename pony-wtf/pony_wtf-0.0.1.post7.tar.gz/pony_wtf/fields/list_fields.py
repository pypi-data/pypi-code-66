
from wtforms import (
    StringField,
    IntegerField,
    FloatField,
    FieldList
)

from wtforms import validators as wtf_validators

class IntListField(FieldList):
    def __init__(self, label=None, validators=None, min_entries=0,
                 max_entries=None, default=tuple(), **kwargs):
        #li_validators = validators.copy()
        """ if wtf_validators.DataRequired in validators:
            validators.pop(wtf_validators.DataRequired, False) """
            
        super(IntListField, self).__init__(

            IntegerField(validators= validators),
            label= label,
            min_entries=min_entries,
            max_entries=max_entries, default=default, **kwargs)
        """ self, unbound_field, label=None, validators=None, min_entries=0,
                 max_entries=None, default=tuple(), **kwargs """

class FloatListField(FieldList):
    def __init__(self, label=None, validators=None, min_entries=0,
                 max_entries=None, default=tuple(), **kwargs):
        super(FloatListField, self).__init__(
            FloatField(validators=validators),
            label, validators, min_entries=min_entries,
            max_entries=max_entries, default=default, **kwargs)


class StrListField(FieldList):
    def __init__(self, label=None, validators=None, min_entries=0,
                 max_entries=None, default=tuple(), **kwargs):
        super(StrListField, self).__init__(
            StringField(validators=validators),
            label, validators, min_entries=min_entries,
            max_entries=max_entries, default=default, **kwargs)
