'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._1499 import ContactPairReporting
    from ._1500 import CoordinateSystemReporting
    from ._1501 import DegreeOfFreedomType
    from ._1502 import ElasticModulusOrthotropicComponents
    from ._1503 import ElementDetailsForFEModel
    from ._1504 import ElementPropertiesBase
    from ._1505 import ElementPropertiesBeam
    from ._1506 import ElementPropertiesInterface
    from ._1507 import ElementPropertiesMass
    from ._1508 import ElementPropertiesRigid
    from ._1509 import ElementPropertiesShell
    from ._1510 import ElementPropertiesSolid
    from ._1511 import ElementPropertiesSpringDashpot
    from ._1512 import ElementPropertiesWithMaterial
    from ._1513 import MaterialPropertiesReporting
    from ._1514 import NodeDetailsForFEModel
    from ._1515 import PoissonRatioOrthotropicComponents
    from ._1516 import RigidElementNodeDegreesOfFreedom
    from ._1517 import ShearModulusOrthotropicComponents
    from ._1518 import ThermalExpansionOrthotropicComponents
