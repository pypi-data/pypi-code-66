'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._1936 import ClutchConnection
    from ._1937 import ClutchSocket
    from ._1938 import ConceptCouplingConnection
    from ._1939 import ConceptCouplingSocket
    from ._1940 import CouplingConnection
    from ._1941 import CouplingSocket
    from ._1942 import PartToPartShearCouplingConnection
    from ._1943 import PartToPartShearCouplingSocket
    from ._1944 import SpringDamperConnection
    from ._1945 import SpringDamperSocket
    from ._1946 import TorqueConverterConnection
    from ._1947 import TorqueConverterPumpSocket
    from ._1948 import TorqueConverterTurbineSocket
