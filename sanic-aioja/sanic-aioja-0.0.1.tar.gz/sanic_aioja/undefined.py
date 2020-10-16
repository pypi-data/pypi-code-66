from jinja2.runtime import ChainableUndefined as ChainableUndefined_
from jinja2.utils import missing, object_type_repr, internalcode


class ChainableUndefined(ChainableUndefined_):
    __slots__ = ()

    def __call__(self, *args, **kwargs):
        return self


class DebugUndefined(ChainableUndefined):
    @internalcode
    def __getattr__(self, name):
        if name[:2] == '__':
            raise AttributeError(name)
        return type(self)(name='%s.%s' % (self._undefined_name, name))

    def __getitem__(self, item):
        return type(self)(name='%s[%s]' % (self._undefined_name, item))

    def __call__(self, *args, **kwargs):
        return type(self)(name='%s()' % self._undefined_name)

    def __str__(self):
        if self._undefined_hint is None:
            if self._undefined_obj is missing:
                return "{{ %s }}" % self._undefined_name
            return "{{ no such element: %s[%r] }}" % (
                object_type_repr(self._undefined_obj),
                self._undefined_name,
            )
        return "{{ undefined value printed: %s }}" % self._undefined_hint
