# поля данных для БД

class BaseField:

    def __init__(self, val, null=False, primery_key=False):
        self.val = val
        self.null = null
        self.primery_key = primery_key
        self.type = 'None'

    def get_query(self):
        query = f'{self.val} {self.type}'
        if self.null:
            query += ' NULL'
        if self.primery_key:
            query += ' PRIMERY_KEY'
        return query

    def __str__(self):
        return self.get_query()


class TextField(BaseField):
    def __init__(self, val, null=False, primery_key=False):
        super().__init__(val, null, primery_key)
        self.type = 'TEXT'


class BlobField(BaseField):
    def __init__(self, val, null=False, primery_key=False):
        super().__init__(val, null, primery_key)
        self.type = 'BLOB'


class IntegerField(BaseField):
    def __init__(self, val, null=False, primery_key=False):
        super().__init__(val, null, primery_key)
        self.type = 'INTEGER'


class RealField(BaseField):
    def __init__(self, val, null=False, primery_key=False):
        super().__init__(val, null, primery_key)
        self.type = 'REAl'


class NoneField(BaseField):
    def __init__(self, val, null=False, primery_key=False):
        super().__init__(val, null, primery_key)
        self.type = 'NONE'


class CustomField(BaseField):
    def __init__(self, val, val_type: str, null=False, primery_key=False):
        super().__init__(val, null, primery_key)
        self.type = val_type.upper()


