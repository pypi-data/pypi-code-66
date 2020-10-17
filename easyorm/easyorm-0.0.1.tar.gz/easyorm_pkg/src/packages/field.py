#

class Field:

    def __init__(self, **args):
        if 'max_length' in args:
            self.max_length = args['max_length']
        
        if 'value' in args:
            self.value = args['value']
        
        if 'required' in args:
            self.required = args['required']

        if 'types' in args['types']:
            self.type = args['types']

    def get(self):
        if len(self.value) > self.max_length:
            raise ValueError('Max value error ')

        if self.value is None and self.required == True:
            raise ValueError('Value has required')

        if self.type != type(self.value):
            raise TypeError('Valeur non conforme')
        return self.value


class CharField(Field):

    def __init__(self, **args):
        super().__init__(**args)
        
    def clean(cls):
        return cls.get()