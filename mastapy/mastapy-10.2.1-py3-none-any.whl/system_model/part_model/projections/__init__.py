'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._2069 import SpecifiedConcentricPartGroupDrawingOrder
    from ._2070 import SpecifiedParallelPartGroupDrawingOrder
