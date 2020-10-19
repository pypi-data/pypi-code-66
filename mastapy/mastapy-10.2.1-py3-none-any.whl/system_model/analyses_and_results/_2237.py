'''_2237.py

CompoundGearWhineAnalysisAnalysis
'''


from typing import Iterable

from mastapy.system_model.part_model import (
    _2024, _2025, _2028, _2030,
    _2031, _2032, _2035, _2036,
    _2039, _2040, _2023, _2041,
    _2044, _2048, _2049, _2050,
    _2052, _2054, _2055, _2057,
    _2058, _2060, _2062, _2063,
    _2064
)
from mastapy.system_model.analyses_and_results.gear_whine_analyses.compound import (
    _5717, _5718, _5723, _5734,
    _5735, _5740, _5751, _5762,
    _5763, _5767, _5722, _5771,
    _5775, _5786, _5787, _5788,
    _5789, _5790, _5796, _5797,
    _5798, _5803, _5807, _5830,
    _5831, _5804, _5744, _5746,
    _5764, _5766, _5719, _5721,
    _5726, _5728, _5729, _5730,
    _5731, _5733, _5747, _5749,
    _5758, _5760, _5761, _5768,
    _5770, _5772, _5774, _5777,
    _5779, _5780, _5782, _5783,
    _5785, _5795, _5808, _5810,
    _5814, _5816, _5817, _5819,
    _5820, _5821, _5832, _5834,
    _5835, _5837, _5791, _5793,
    _5725, _5736, _5738, _5741,
    _5743, _5752, _5754, _5756,
    _5757, _5799, _5805, _5801,
    _5800, _5811, _5813, _5822,
    _5823, _5824, _5825, _5826,
    _5828, _5829, _5755, _5724,
    _5739, _5750, _5776, _5794,
    _5802, _5806, _5727, _5745,
    _5765, _5815, _5732, _5748,
    _5720, _5759, _5773, _5778,
    _5781, _5784, _5809, _5818,
    _5833, _5836, _5769, _5792,
    _5737, _5742, _5753, _5812,
    _5827
)
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.shaft_model import _2067
from mastapy.system_model.part_model.gears import (
    _2105, _2106, _2112, _2113,
    _2097, _2098, _2099, _2100,
    _2101, _2102, _2103, _2104,
    _2107, _2108, _2109, _2110,
    _2111, _2114, _2116, _2118,
    _2119, _2120, _2121, _2122,
    _2123, _2124, _2125, _2126,
    _2127, _2128, _2129, _2130,
    _2131, _2132, _2133, _2134,
    _2135, _2136, _2137, _2138
)
from mastapy.system_model.part_model.couplings import (
    _2167, _2168, _2156, _2158,
    _2159, _2161, _2162, _2163,
    _2164, _2165, _2166, _2169,
    _2177, _2175, _2176, _2178,
    _2179, _2180, _2182, _2183,
    _2184, _2185, _2186, _2188
)
from mastapy.system_model.connections_and_sockets import (
    _1879, _1874, _1875, _1878,
    _1887, _1890, _1894, _1898
)
from mastapy.system_model.connections_and_sockets.gears import (
    _1904, _1908, _1914, _1928,
    _1906, _1910, _1902, _1912,
    _1918, _1921, _1922, _1923,
    _1926, _1930, _1932, _1934,
    _1916
)
from mastapy.system_model.connections_and_sockets.couplings import (
    _1942, _1936, _1938, _1940,
    _1944, _1946
)
from mastapy._internal.python_net import python_net_import
from mastapy.system_model.analyses_and_results import _2197

_ABSTRACT_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'AbstractAssembly')
_ABSTRACT_SHAFT_OR_HOUSING = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'AbstractShaftOrHousing')
_BEARING = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Bearing')
_BOLT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Bolt')
_BOLTED_JOINT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'BoltedJoint')
_COMPONENT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Component')
_CONNECTOR = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Connector')
_DATUM = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Datum')
_EXTERNAL_CAD_MODEL = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'ExternalCADModel')
_FLEXIBLE_PIN_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'FlexiblePinAssembly')
_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Assembly')
_GUIDE_DXF_MODEL = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'GuideDxfModel')
_IMPORTED_FE_COMPONENT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'ImportedFEComponent')
_MASS_DISC = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'MassDisc')
_MEASUREMENT_COMPONENT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'MeasurementComponent')
_MOUNTABLE_COMPONENT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'MountableComponent')
_OIL_SEAL = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'OilSeal')
_PART = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Part')
_PLANET_CARRIER = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'PlanetCarrier')
_POINT_LOAD = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'PointLoad')
_POWER_LOAD = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'PowerLoad')
_ROOT_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'RootAssembly')
_SPECIALISED_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'SpecialisedAssembly')
_UNBALANCED_MASS = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'UnbalancedMass')
_VIRTUAL_COMPONENT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'VirtualComponent')
_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.PartModel.ShaftModel', 'Shaft')
_CONCEPT_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ConceptGear')
_CONCEPT_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ConceptGearSet')
_FACE_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'FaceGear')
_FACE_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'FaceGearSet')
_AGMA_GLEASON_CONICAL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'AGMAGleasonConicalGear')
_AGMA_GLEASON_CONICAL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'AGMAGleasonConicalGearSet')
_BEVEL_DIFFERENTIAL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'BevelDifferentialGear')
_BEVEL_DIFFERENTIAL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'BevelDifferentialGearSet')
_BEVEL_DIFFERENTIAL_PLANET_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'BevelDifferentialPlanetGear')
_BEVEL_DIFFERENTIAL_SUN_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'BevelDifferentialSunGear')
_BEVEL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'BevelGear')
_BEVEL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'BevelGearSet')
_CONICAL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ConicalGear')
_CONICAL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ConicalGearSet')
_CYLINDRICAL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'CylindricalGear')
_CYLINDRICAL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'CylindricalGearSet')
_CYLINDRICAL_PLANET_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'CylindricalPlanetGear')
_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'Gear')
_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'GearSet')
_HYPOID_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'HypoidGear')
_HYPOID_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'HypoidGearSet')
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'KlingelnbergCycloPalloidConicalGear')
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'KlingelnbergCycloPalloidConicalGearSet')
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'KlingelnbergCycloPalloidHypoidGear')
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'KlingelnbergCycloPalloidHypoidGearSet')
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'KlingelnbergCycloPalloidSpiralBevelGear')
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'KlingelnbergCycloPalloidSpiralBevelGearSet')
_PLANETARY_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'PlanetaryGearSet')
_SPIRAL_BEVEL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'SpiralBevelGear')
_SPIRAL_BEVEL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'SpiralBevelGearSet')
_STRAIGHT_BEVEL_DIFF_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'StraightBevelDiffGear')
_STRAIGHT_BEVEL_DIFF_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'StraightBevelDiffGearSet')
_STRAIGHT_BEVEL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'StraightBevelGear')
_STRAIGHT_BEVEL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'StraightBevelGearSet')
_STRAIGHT_BEVEL_PLANET_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'StraightBevelPlanetGear')
_STRAIGHT_BEVEL_SUN_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'StraightBevelSunGear')
_WORM_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'WormGear')
_WORM_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'WormGearSet')
_ZEROL_BEVEL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ZerolBevelGear')
_ZEROL_BEVEL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ZerolBevelGearSet')
_PART_TO_PART_SHEAR_COUPLING = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'PartToPartShearCoupling')
_PART_TO_PART_SHEAR_COUPLING_HALF = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'PartToPartShearCouplingHalf')
_BELT_DRIVE = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'BeltDrive')
_CLUTCH = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'Clutch')
_CLUTCH_HALF = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'ClutchHalf')
_CONCEPT_COUPLING = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'ConceptCoupling')
_CONCEPT_COUPLING_HALF = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'ConceptCouplingHalf')
_COUPLING = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'Coupling')
_COUPLING_HALF = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'CouplingHalf')
_CVT = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'CVT')
_CVT_PULLEY = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'CVTPulley')
_PULLEY = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'Pulley')
_SHAFT_HUB_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'ShaftHubConnection')
_ROLLING_RING = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'RollingRing')
_ROLLING_RING_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'RollingRingAssembly')
_SPRING_DAMPER = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'SpringDamper')
_SPRING_DAMPER_HALF = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'SpringDamperHalf')
_SYNCHRONISER = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'Synchroniser')
_SYNCHRONISER_HALF = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'SynchroniserHalf')
_SYNCHRONISER_PART = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'SynchroniserPart')
_SYNCHRONISER_SLEEVE = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'SynchroniserSleeve')
_TORQUE_CONVERTER = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'TorqueConverter')
_TORQUE_CONVERTER_PUMP = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'TorqueConverterPump')
_TORQUE_CONVERTER_TURBINE = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'TorqueConverterTurbine')
_CVT_BELT_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'CVTBeltConnection')
_BELT_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'BeltConnection')
_COAXIAL_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'CoaxialConnection')
_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'Connection')
_INTER_MOUNTABLE_COMPONENT_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'InterMountableComponentConnection')
_PLANETARY_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'PlanetaryConnection')
_ROLLING_RING_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'RollingRingConnection')
_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'ShaftToMountableComponentConnection')
_BEVEL_DIFFERENTIAL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'BevelDifferentialGearMesh')
_CONCEPT_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'ConceptGearMesh')
_FACE_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'FaceGearMesh')
_STRAIGHT_BEVEL_DIFF_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'StraightBevelDiffGearMesh')
_BEVEL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'BevelGearMesh')
_CONICAL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'ConicalGearMesh')
_AGMA_GLEASON_CONICAL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'AGMAGleasonConicalGearMesh')
_CYLINDRICAL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'CylindricalGearMesh')
_HYPOID_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'HypoidGearMesh')
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'KlingelnbergCycloPalloidConicalGearMesh')
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'KlingelnbergCycloPalloidHypoidGearMesh')
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'KlingelnbergCycloPalloidSpiralBevelGearMesh')
_SPIRAL_BEVEL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'SpiralBevelGearMesh')
_STRAIGHT_BEVEL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'StraightBevelGearMesh')
_WORM_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'WormGearMesh')
_ZEROL_BEVEL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'ZerolBevelGearMesh')
_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'GearMesh')
_PART_TO_PART_SHEAR_COUPLING_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'PartToPartShearCouplingConnection')
_CLUTCH_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'ClutchConnection')
_CONCEPT_COUPLING_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'ConceptCouplingConnection')
_COUPLING_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'CouplingConnection')
_SPRING_DAMPER_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'SpringDamperConnection')
_TORQUE_CONVERTER_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'TorqueConverterConnection')
_COMPOUND_GEAR_WHINE_ANALYSIS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'CompoundGearWhineAnalysisAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CompoundGearWhineAnalysisAnalysis',)


class CompoundGearWhineAnalysisAnalysis(_2197.CompoundAnalysis):
    '''CompoundGearWhineAnalysisAnalysis

    This is a mastapy class.
    '''

    TYPE = _COMPOUND_GEAR_WHINE_ANALYSIS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CompoundGearWhineAnalysisAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    def results_for_abstract_assembly(self, design_entity: '_2024.AbstractAssembly') -> 'Iterable[_5717.AbstractAssemblyCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.AbstractAssemblyCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ABSTRACT_ASSEMBLY](design_entity.wrapped if design_entity else None), constructor.new(_5717.AbstractAssemblyCompoundGearWhineAnalysis))

    def results_for_abstract_shaft_or_housing(self, design_entity: '_2025.AbstractShaftOrHousing') -> 'Iterable[_5718.AbstractShaftOrHousingCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaftOrHousing)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.AbstractShaftOrHousingCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT_OR_HOUSING](design_entity.wrapped if design_entity else None), constructor.new(_5718.AbstractShaftOrHousingCompoundGearWhineAnalysis))

    def results_for_bearing(self, design_entity: '_2028.Bearing') -> 'Iterable[_5723.BearingCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bearing)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BearingCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEARING](design_entity.wrapped if design_entity else None), constructor.new(_5723.BearingCompoundGearWhineAnalysis))

    def results_for_bolt(self, design_entity: '_2030.Bolt') -> 'Iterable[_5734.BoltCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bolt)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BoltCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BOLT](design_entity.wrapped if design_entity else None), constructor.new(_5734.BoltCompoundGearWhineAnalysis))

    def results_for_bolted_joint(self, design_entity: '_2031.BoltedJoint') -> 'Iterable[_5735.BoltedJointCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.BoltedJoint)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BoltedJointCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BOLTED_JOINT](design_entity.wrapped if design_entity else None), constructor.new(_5735.BoltedJointCompoundGearWhineAnalysis))

    def results_for_component(self, design_entity: '_2032.Component') -> 'Iterable[_5740.ComponentCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Component)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ComponentCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_COMPONENT](design_entity.wrapped if design_entity else None), constructor.new(_5740.ComponentCompoundGearWhineAnalysis))

    def results_for_connector(self, design_entity: '_2035.Connector') -> 'Iterable[_5751.ConnectorCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Connector)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ConnectorCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONNECTOR](design_entity.wrapped if design_entity else None), constructor.new(_5751.ConnectorCompoundGearWhineAnalysis))

    def results_for_datum(self, design_entity: '_2036.Datum') -> 'Iterable[_5762.DatumCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Datum)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.DatumCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_DATUM](design_entity.wrapped if design_entity else None), constructor.new(_5762.DatumCompoundGearWhineAnalysis))

    def results_for_external_cad_model(self, design_entity: '_2039.ExternalCADModel') -> 'Iterable[_5763.ExternalCADModelCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ExternalCADModel)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ExternalCADModelCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_EXTERNAL_CAD_MODEL](design_entity.wrapped if design_entity else None), constructor.new(_5763.ExternalCADModelCompoundGearWhineAnalysis))

    def results_for_flexible_pin_assembly(self, design_entity: '_2040.FlexiblePinAssembly') -> 'Iterable[_5767.FlexiblePinAssemblyCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.FlexiblePinAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.FlexiblePinAssemblyCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_FLEXIBLE_PIN_ASSEMBLY](design_entity.wrapped if design_entity else None), constructor.new(_5767.FlexiblePinAssemblyCompoundGearWhineAnalysis))

    def results_for_assembly(self, design_entity: '_2023.Assembly') -> 'Iterable[_5722.AssemblyCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Assembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.AssemblyCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ASSEMBLY](design_entity.wrapped if design_entity else None), constructor.new(_5722.AssemblyCompoundGearWhineAnalysis))

    def results_for_guide_dxf_model(self, design_entity: '_2041.GuideDxfModel') -> 'Iterable[_5771.GuideDxfModelCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.GuideDxfModel)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.GuideDxfModelCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_GUIDE_DXF_MODEL](design_entity.wrapped if design_entity else None), constructor.new(_5771.GuideDxfModelCompoundGearWhineAnalysis))

    def results_for_imported_fe_component(self, design_entity: '_2044.ImportedFEComponent') -> 'Iterable[_5775.ImportedFEComponentCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ImportedFEComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ImportedFEComponentCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_IMPORTED_FE_COMPONENT](design_entity.wrapped if design_entity else None), constructor.new(_5775.ImportedFEComponentCompoundGearWhineAnalysis))

    def results_for_mass_disc(self, design_entity: '_2048.MassDisc') -> 'Iterable[_5786.MassDiscCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MassDisc)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.MassDiscCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_MASS_DISC](design_entity.wrapped if design_entity else None), constructor.new(_5786.MassDiscCompoundGearWhineAnalysis))

    def results_for_measurement_component(self, design_entity: '_2049.MeasurementComponent') -> 'Iterable[_5787.MeasurementComponentCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MeasurementComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.MeasurementComponentCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_MEASUREMENT_COMPONENT](design_entity.wrapped if design_entity else None), constructor.new(_5787.MeasurementComponentCompoundGearWhineAnalysis))

    def results_for_mountable_component(self, design_entity: '_2050.MountableComponent') -> 'Iterable[_5788.MountableComponentCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MountableComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.MountableComponentCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_MOUNTABLE_COMPONENT](design_entity.wrapped if design_entity else None), constructor.new(_5788.MountableComponentCompoundGearWhineAnalysis))

    def results_for_oil_seal(self, design_entity: '_2052.OilSeal') -> 'Iterable[_5789.OilSealCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.OilSeal)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.OilSealCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_OIL_SEAL](design_entity.wrapped if design_entity else None), constructor.new(_5789.OilSealCompoundGearWhineAnalysis))

    def results_for_part(self, design_entity: '_2054.Part') -> 'Iterable[_5790.PartCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Part)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.PartCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PART](design_entity.wrapped if design_entity else None), constructor.new(_5790.PartCompoundGearWhineAnalysis))

    def results_for_planet_carrier(self, design_entity: '_2055.PlanetCarrier') -> 'Iterable[_5796.PlanetCarrierCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PlanetCarrier)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.PlanetCarrierCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PLANET_CARRIER](design_entity.wrapped if design_entity else None), constructor.new(_5796.PlanetCarrierCompoundGearWhineAnalysis))

    def results_for_point_load(self, design_entity: '_2057.PointLoad') -> 'Iterable[_5797.PointLoadCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PointLoad)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.PointLoadCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_POINT_LOAD](design_entity.wrapped if design_entity else None), constructor.new(_5797.PointLoadCompoundGearWhineAnalysis))

    def results_for_power_load(self, design_entity: '_2058.PowerLoad') -> 'Iterable[_5798.PowerLoadCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PowerLoad)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.PowerLoadCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_POWER_LOAD](design_entity.wrapped if design_entity else None), constructor.new(_5798.PowerLoadCompoundGearWhineAnalysis))

    def results_for_root_assembly(self, design_entity: '_2060.RootAssembly') -> 'Iterable[_5803.RootAssemblyCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.RootAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.RootAssemblyCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ROOT_ASSEMBLY](design_entity.wrapped if design_entity else None), constructor.new(_5803.RootAssemblyCompoundGearWhineAnalysis))

    def results_for_specialised_assembly(self, design_entity: '_2062.SpecialisedAssembly') -> 'Iterable[_5807.SpecialisedAssemblyCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.SpecialisedAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.SpecialisedAssemblyCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SPECIALISED_ASSEMBLY](design_entity.wrapped if design_entity else None), constructor.new(_5807.SpecialisedAssemblyCompoundGearWhineAnalysis))

    def results_for_unbalanced_mass(self, design_entity: '_2063.UnbalancedMass') -> 'Iterable[_5830.UnbalancedMassCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.UnbalancedMass)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.UnbalancedMassCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_UNBALANCED_MASS](design_entity.wrapped if design_entity else None), constructor.new(_5830.UnbalancedMassCompoundGearWhineAnalysis))

    def results_for_virtual_component(self, design_entity: '_2064.VirtualComponent') -> 'Iterable[_5831.VirtualComponentCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.VirtualComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.VirtualComponentCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_VIRTUAL_COMPONENT](design_entity.wrapped if design_entity else None), constructor.new(_5831.VirtualComponentCompoundGearWhineAnalysis))

    def results_for_shaft(self, design_entity: '_2067.Shaft') -> 'Iterable[_5804.ShaftCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.shaft_model.Shaft)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ShaftCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SHAFT](design_entity.wrapped if design_entity else None), constructor.new(_5804.ShaftCompoundGearWhineAnalysis))

    def results_for_concept_gear(self, design_entity: '_2105.ConceptGear') -> 'Iterable[_5744.ConceptGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ConceptGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5744.ConceptGearCompoundGearWhineAnalysis))

    def results_for_concept_gear_set(self, design_entity: '_2106.ConceptGearSet') -> 'Iterable[_5746.ConceptGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ConceptGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5746.ConceptGearSetCompoundGearWhineAnalysis))

    def results_for_face_gear(self, design_entity: '_2112.FaceGear') -> 'Iterable[_5764.FaceGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.FaceGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_FACE_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5764.FaceGearCompoundGearWhineAnalysis))

    def results_for_face_gear_set(self, design_entity: '_2113.FaceGearSet') -> 'Iterable[_5766.FaceGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.FaceGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_FACE_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5766.FaceGearSetCompoundGearWhineAnalysis))

    def results_for_agma_gleason_conical_gear(self, design_entity: '_2097.AGMAGleasonConicalGear') -> 'Iterable[_5719.AGMAGleasonConicalGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.AGMAGleasonConicalGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5719.AGMAGleasonConicalGearCompoundGearWhineAnalysis))

    def results_for_agma_gleason_conical_gear_set(self, design_entity: '_2098.AGMAGleasonConicalGearSet') -> 'Iterable[_5721.AGMAGleasonConicalGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.AGMAGleasonConicalGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5721.AGMAGleasonConicalGearSetCompoundGearWhineAnalysis))

    def results_for_bevel_differential_gear(self, design_entity: '_2099.BevelDifferentialGear') -> 'Iterable[_5726.BevelDifferentialGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BevelDifferentialGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5726.BevelDifferentialGearCompoundGearWhineAnalysis))

    def results_for_bevel_differential_gear_set(self, design_entity: '_2100.BevelDifferentialGearSet') -> 'Iterable[_5728.BevelDifferentialGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BevelDifferentialGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5728.BevelDifferentialGearSetCompoundGearWhineAnalysis))

    def results_for_bevel_differential_planet_gear(self, design_entity: '_2101.BevelDifferentialPlanetGear') -> 'Iterable[_5729.BevelDifferentialPlanetGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BevelDifferentialPlanetGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_PLANET_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5729.BevelDifferentialPlanetGearCompoundGearWhineAnalysis))

    def results_for_bevel_differential_sun_gear(self, design_entity: '_2102.BevelDifferentialSunGear') -> 'Iterable[_5730.BevelDifferentialSunGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialSunGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BevelDifferentialSunGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_SUN_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5730.BevelDifferentialSunGearCompoundGearWhineAnalysis))

    def results_for_bevel_gear(self, design_entity: '_2103.BevelGear') -> 'Iterable[_5731.BevelGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BevelGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5731.BevelGearCompoundGearWhineAnalysis))

    def results_for_bevel_gear_set(self, design_entity: '_2104.BevelGearSet') -> 'Iterable[_5733.BevelGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BevelGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5733.BevelGearSetCompoundGearWhineAnalysis))

    def results_for_conical_gear(self, design_entity: '_2107.ConicalGear') -> 'Iterable[_5747.ConicalGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ConicalGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5747.ConicalGearCompoundGearWhineAnalysis))

    def results_for_conical_gear_set(self, design_entity: '_2108.ConicalGearSet') -> 'Iterable[_5749.ConicalGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ConicalGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5749.ConicalGearSetCompoundGearWhineAnalysis))

    def results_for_cylindrical_gear(self, design_entity: '_2109.CylindricalGear') -> 'Iterable[_5758.CylindricalGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.CylindricalGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5758.CylindricalGearCompoundGearWhineAnalysis))

    def results_for_cylindrical_gear_set(self, design_entity: '_2110.CylindricalGearSet') -> 'Iterable[_5760.CylindricalGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.CylindricalGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5760.CylindricalGearSetCompoundGearWhineAnalysis))

    def results_for_cylindrical_planet_gear(self, design_entity: '_2111.CylindricalPlanetGear') -> 'Iterable[_5761.CylindricalPlanetGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalPlanetGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.CylindricalPlanetGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_PLANET_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5761.CylindricalPlanetGearCompoundGearWhineAnalysis))

    def results_for_gear(self, design_entity: '_2114.Gear') -> 'Iterable[_5768.GearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.Gear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.GearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5768.GearCompoundGearWhineAnalysis))

    def results_for_gear_set(self, design_entity: '_2116.GearSet') -> 'Iterable[_5770.GearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.GearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.GearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5770.GearSetCompoundGearWhineAnalysis))

    def results_for_hypoid_gear(self, design_entity: '_2118.HypoidGear') -> 'Iterable[_5772.HypoidGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.HypoidGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5772.HypoidGearCompoundGearWhineAnalysis))

    def results_for_hypoid_gear_set(self, design_entity: '_2119.HypoidGearSet') -> 'Iterable[_5774.HypoidGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.HypoidGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5774.HypoidGearSetCompoundGearWhineAnalysis))

    def results_for_klingelnberg_cyclo_palloid_conical_gear(self, design_entity: '_2120.KlingelnbergCycloPalloidConicalGear') -> 'Iterable[_5777.KlingelnbergCycloPalloidConicalGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.KlingelnbergCycloPalloidConicalGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5777.KlingelnbergCycloPalloidConicalGearCompoundGearWhineAnalysis))

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set(self, design_entity: '_2121.KlingelnbergCycloPalloidConicalGearSet') -> 'Iterable[_5779.KlingelnbergCycloPalloidConicalGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.KlingelnbergCycloPalloidConicalGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5779.KlingelnbergCycloPalloidConicalGearSetCompoundGearWhineAnalysis))

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear(self, design_entity: '_2122.KlingelnbergCycloPalloidHypoidGear') -> 'Iterable[_5780.KlingelnbergCycloPalloidHypoidGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.KlingelnbergCycloPalloidHypoidGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5780.KlingelnbergCycloPalloidHypoidGearCompoundGearWhineAnalysis))

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set(self, design_entity: '_2123.KlingelnbergCycloPalloidHypoidGearSet') -> 'Iterable[_5782.KlingelnbergCycloPalloidHypoidGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.KlingelnbergCycloPalloidHypoidGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5782.KlingelnbergCycloPalloidHypoidGearSetCompoundGearWhineAnalysis))

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(self, design_entity: '_2124.KlingelnbergCycloPalloidSpiralBevelGear') -> 'Iterable[_5783.KlingelnbergCycloPalloidSpiralBevelGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5783.KlingelnbergCycloPalloidSpiralBevelGearCompoundGearWhineAnalysis))

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self, design_entity: '_2125.KlingelnbergCycloPalloidSpiralBevelGearSet') -> 'Iterable[_5785.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5785.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundGearWhineAnalysis))

    def results_for_planetary_gear_set(self, design_entity: '_2126.PlanetaryGearSet') -> 'Iterable[_5795.PlanetaryGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.PlanetaryGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.PlanetaryGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PLANETARY_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5795.PlanetaryGearSetCompoundGearWhineAnalysis))

    def results_for_spiral_bevel_gear(self, design_entity: '_2127.SpiralBevelGear') -> 'Iterable[_5808.SpiralBevelGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.SpiralBevelGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5808.SpiralBevelGearCompoundGearWhineAnalysis))

    def results_for_spiral_bevel_gear_set(self, design_entity: '_2128.SpiralBevelGearSet') -> 'Iterable[_5810.SpiralBevelGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.SpiralBevelGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5810.SpiralBevelGearSetCompoundGearWhineAnalysis))

    def results_for_straight_bevel_diff_gear(self, design_entity: '_2129.StraightBevelDiffGear') -> 'Iterable[_5814.StraightBevelDiffGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.StraightBevelDiffGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5814.StraightBevelDiffGearCompoundGearWhineAnalysis))

    def results_for_straight_bevel_diff_gear_set(self, design_entity: '_2130.StraightBevelDiffGearSet') -> 'Iterable[_5816.StraightBevelDiffGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.StraightBevelDiffGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5816.StraightBevelDiffGearSetCompoundGearWhineAnalysis))

    def results_for_straight_bevel_gear(self, design_entity: '_2131.StraightBevelGear') -> 'Iterable[_5817.StraightBevelGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.StraightBevelGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5817.StraightBevelGearCompoundGearWhineAnalysis))

    def results_for_straight_bevel_gear_set(self, design_entity: '_2132.StraightBevelGearSet') -> 'Iterable[_5819.StraightBevelGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.StraightBevelGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5819.StraightBevelGearSetCompoundGearWhineAnalysis))

    def results_for_straight_bevel_planet_gear(self, design_entity: '_2133.StraightBevelPlanetGear') -> 'Iterable[_5820.StraightBevelPlanetGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelPlanetGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.StraightBevelPlanetGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_PLANET_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5820.StraightBevelPlanetGearCompoundGearWhineAnalysis))

    def results_for_straight_bevel_sun_gear(self, design_entity: '_2134.StraightBevelSunGear') -> 'Iterable[_5821.StraightBevelSunGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelSunGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.StraightBevelSunGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_SUN_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5821.StraightBevelSunGearCompoundGearWhineAnalysis))

    def results_for_worm_gear(self, design_entity: '_2135.WormGear') -> 'Iterable[_5832.WormGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.WormGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_WORM_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5832.WormGearCompoundGearWhineAnalysis))

    def results_for_worm_gear_set(self, design_entity: '_2136.WormGearSet') -> 'Iterable[_5834.WormGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.WormGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_WORM_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5834.WormGearSetCompoundGearWhineAnalysis))

    def results_for_zerol_bevel_gear(self, design_entity: '_2137.ZerolBevelGear') -> 'Iterable[_5835.ZerolBevelGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ZerolBevelGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR](design_entity.wrapped if design_entity else None), constructor.new(_5835.ZerolBevelGearCompoundGearWhineAnalysis))

    def results_for_zerol_bevel_gear_set(self, design_entity: '_2138.ZerolBevelGearSet') -> 'Iterable[_5837.ZerolBevelGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ZerolBevelGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR_SET](design_entity.wrapped if design_entity else None), constructor.new(_5837.ZerolBevelGearSetCompoundGearWhineAnalysis))

    def results_for_part_to_part_shear_coupling(self, design_entity: '_2167.PartToPartShearCoupling') -> 'Iterable[_5791.PartToPartShearCouplingCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCoupling)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.PartToPartShearCouplingCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING](design_entity.wrapped if design_entity else None), constructor.new(_5791.PartToPartShearCouplingCompoundGearWhineAnalysis))

    def results_for_part_to_part_shear_coupling_half(self, design_entity: '_2168.PartToPartShearCouplingHalf') -> 'Iterable[_5793.PartToPartShearCouplingHalfCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.PartToPartShearCouplingHalfCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING_HALF](design_entity.wrapped if design_entity else None), constructor.new(_5793.PartToPartShearCouplingHalfCompoundGearWhineAnalysis))

    def results_for_belt_drive(self, design_entity: '_2156.BeltDrive') -> 'Iterable[_5725.BeltDriveCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.BeltDrive)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BeltDriveCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BELT_DRIVE](design_entity.wrapped if design_entity else None), constructor.new(_5725.BeltDriveCompoundGearWhineAnalysis))

    def results_for_clutch(self, design_entity: '_2158.Clutch') -> 'Iterable[_5736.ClutchCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Clutch)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ClutchCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CLUTCH](design_entity.wrapped if design_entity else None), constructor.new(_5736.ClutchCompoundGearWhineAnalysis))

    def results_for_clutch_half(self, design_entity: '_2159.ClutchHalf') -> 'Iterable[_5738.ClutchHalfCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ClutchHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ClutchHalfCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CLUTCH_HALF](design_entity.wrapped if design_entity else None), constructor.new(_5738.ClutchHalfCompoundGearWhineAnalysis))

    def results_for_concept_coupling(self, design_entity: '_2161.ConceptCoupling') -> 'Iterable[_5741.ConceptCouplingCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCoupling)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ConceptCouplingCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING](design_entity.wrapped if design_entity else None), constructor.new(_5741.ConceptCouplingCompoundGearWhineAnalysis))

    def results_for_concept_coupling_half(self, design_entity: '_2162.ConceptCouplingHalf') -> 'Iterable[_5743.ConceptCouplingHalfCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCouplingHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ConceptCouplingHalfCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING_HALF](design_entity.wrapped if design_entity else None), constructor.new(_5743.ConceptCouplingHalfCompoundGearWhineAnalysis))

    def results_for_coupling(self, design_entity: '_2163.Coupling') -> 'Iterable[_5752.CouplingCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Coupling)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.CouplingCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_COUPLING](design_entity.wrapped if design_entity else None), constructor.new(_5752.CouplingCompoundGearWhineAnalysis))

    def results_for_coupling_half(self, design_entity: '_2164.CouplingHalf') -> 'Iterable[_5754.CouplingHalfCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CouplingHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.CouplingHalfCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_COUPLING_HALF](design_entity.wrapped if design_entity else None), constructor.new(_5754.CouplingHalfCompoundGearWhineAnalysis))

    def results_for_cvt(self, design_entity: '_2165.CVT') -> 'Iterable[_5756.CVTCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVT)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.CVTCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CVT](design_entity.wrapped if design_entity else None), constructor.new(_5756.CVTCompoundGearWhineAnalysis))

    def results_for_cvt_pulley(self, design_entity: '_2166.CVTPulley') -> 'Iterable[_5757.CVTPulleyCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVTPulley)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.CVTPulleyCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CVT_PULLEY](design_entity.wrapped if design_entity else None), constructor.new(_5757.CVTPulleyCompoundGearWhineAnalysis))

    def results_for_pulley(self, design_entity: '_2169.Pulley') -> 'Iterable[_5799.PulleyCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Pulley)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.PulleyCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PULLEY](design_entity.wrapped if design_entity else None), constructor.new(_5799.PulleyCompoundGearWhineAnalysis))

    def results_for_shaft_hub_connection(self, design_entity: '_2177.ShaftHubConnection') -> 'Iterable[_5805.ShaftHubConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ShaftHubConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ShaftHubConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SHAFT_HUB_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5805.ShaftHubConnectionCompoundGearWhineAnalysis))

    def results_for_rolling_ring(self, design_entity: '_2175.RollingRing') -> 'Iterable[_5801.RollingRingCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRing)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.RollingRingCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ROLLING_RING](design_entity.wrapped if design_entity else None), constructor.new(_5801.RollingRingCompoundGearWhineAnalysis))

    def results_for_rolling_ring_assembly(self, design_entity: '_2176.RollingRingAssembly') -> 'Iterable[_5800.RollingRingAssemblyCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRingAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.RollingRingAssemblyCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ROLLING_RING_ASSEMBLY](design_entity.wrapped if design_entity else None), constructor.new(_5800.RollingRingAssemblyCompoundGearWhineAnalysis))

    def results_for_spring_damper(self, design_entity: '_2178.SpringDamper') -> 'Iterable[_5811.SpringDamperCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamper)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.SpringDamperCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER](design_entity.wrapped if design_entity else None), constructor.new(_5811.SpringDamperCompoundGearWhineAnalysis))

    def results_for_spring_damper_half(self, design_entity: '_2179.SpringDamperHalf') -> 'Iterable[_5813.SpringDamperHalfCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamperHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.SpringDamperHalfCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER_HALF](design_entity.wrapped if design_entity else None), constructor.new(_5813.SpringDamperHalfCompoundGearWhineAnalysis))

    def results_for_synchroniser(self, design_entity: '_2180.Synchroniser') -> 'Iterable[_5822.SynchroniserCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Synchroniser)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.SynchroniserCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SYNCHRONISER](design_entity.wrapped if design_entity else None), constructor.new(_5822.SynchroniserCompoundGearWhineAnalysis))

    def results_for_synchroniser_half(self, design_entity: '_2182.SynchroniserHalf') -> 'Iterable[_5823.SynchroniserHalfCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.SynchroniserHalfCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_HALF](design_entity.wrapped if design_entity else None), constructor.new(_5823.SynchroniserHalfCompoundGearWhineAnalysis))

    def results_for_synchroniser_part(self, design_entity: '_2183.SynchroniserPart') -> 'Iterable[_5824.SynchroniserPartCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserPart)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.SynchroniserPartCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_PART](design_entity.wrapped if design_entity else None), constructor.new(_5824.SynchroniserPartCompoundGearWhineAnalysis))

    def results_for_synchroniser_sleeve(self, design_entity: '_2184.SynchroniserSleeve') -> 'Iterable[_5825.SynchroniserSleeveCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserSleeve)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.SynchroniserSleeveCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_SLEEVE](design_entity.wrapped if design_entity else None), constructor.new(_5825.SynchroniserSleeveCompoundGearWhineAnalysis))

    def results_for_torque_converter(self, design_entity: '_2185.TorqueConverter') -> 'Iterable[_5826.TorqueConverterCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverter)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.TorqueConverterCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER](design_entity.wrapped if design_entity else None), constructor.new(_5826.TorqueConverterCompoundGearWhineAnalysis))

    def results_for_torque_converter_pump(self, design_entity: '_2186.TorqueConverterPump') -> 'Iterable[_5828.TorqueConverterPumpCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterPump)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.TorqueConverterPumpCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_PUMP](design_entity.wrapped if design_entity else None), constructor.new(_5828.TorqueConverterPumpCompoundGearWhineAnalysis))

    def results_for_torque_converter_turbine(self, design_entity: '_2188.TorqueConverterTurbine') -> 'Iterable[_5829.TorqueConverterTurbineCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterTurbine)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.TorqueConverterTurbineCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_TURBINE](design_entity.wrapped if design_entity else None), constructor.new(_5829.TorqueConverterTurbineCompoundGearWhineAnalysis))

    def results_for_cvt_belt_connection(self, design_entity: '_1879.CVTBeltConnection') -> 'Iterable[_5755.CVTBeltConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CVTBeltConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.CVTBeltConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CVT_BELT_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5755.CVTBeltConnectionCompoundGearWhineAnalysis))

    def results_for_belt_connection(self, design_entity: '_1874.BeltConnection') -> 'Iterable[_5724.BeltConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.BeltConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BeltConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BELT_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5724.BeltConnectionCompoundGearWhineAnalysis))

    def results_for_coaxial_connection(self, design_entity: '_1875.CoaxialConnection') -> 'Iterable[_5739.CoaxialConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CoaxialConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.CoaxialConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_COAXIAL_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5739.CoaxialConnectionCompoundGearWhineAnalysis))

    def results_for_connection(self, design_entity: '_1878.Connection') -> 'Iterable[_5750.ConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.Connection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5750.ConnectionCompoundGearWhineAnalysis))

    def results_for_inter_mountable_component_connection(self, design_entity: '_1887.InterMountableComponentConnection') -> 'Iterable[_5776.InterMountableComponentConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.InterMountableComponentConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.InterMountableComponentConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_INTER_MOUNTABLE_COMPONENT_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5776.InterMountableComponentConnectionCompoundGearWhineAnalysis))

    def results_for_planetary_connection(self, design_entity: '_1890.PlanetaryConnection') -> 'Iterable[_5794.PlanetaryConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.PlanetaryConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.PlanetaryConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PLANETARY_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5794.PlanetaryConnectionCompoundGearWhineAnalysis))

    def results_for_rolling_ring_connection(self, design_entity: '_1894.RollingRingConnection') -> 'Iterable[_5802.RollingRingConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.RollingRingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.RollingRingConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ROLLING_RING_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5802.RollingRingConnectionCompoundGearWhineAnalysis))

    def results_for_shaft_to_mountable_component_connection(self, design_entity: '_1898.ShaftToMountableComponentConnection') -> 'Iterable[_5806.ShaftToMountableComponentConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ShaftToMountableComponentConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5806.ShaftToMountableComponentConnectionCompoundGearWhineAnalysis))

    def results_for_bevel_differential_gear_mesh(self, design_entity: '_1904.BevelDifferentialGearMesh') -> 'Iterable[_5727.BevelDifferentialGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BevelDifferentialGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5727.BevelDifferentialGearMeshCompoundGearWhineAnalysis))

    def results_for_concept_gear_mesh(self, design_entity: '_1908.ConceptGearMesh') -> 'Iterable[_5745.ConceptGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ConceptGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5745.ConceptGearMeshCompoundGearWhineAnalysis))

    def results_for_face_gear_mesh(self, design_entity: '_1914.FaceGearMesh') -> 'Iterable[_5765.FaceGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.FaceGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.FaceGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_FACE_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5765.FaceGearMeshCompoundGearWhineAnalysis))

    def results_for_straight_bevel_diff_gear_mesh(self, design_entity: '_1928.StraightBevelDiffGearMesh') -> 'Iterable[_5815.StraightBevelDiffGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.StraightBevelDiffGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5815.StraightBevelDiffGearMeshCompoundGearWhineAnalysis))

    def results_for_bevel_gear_mesh(self, design_entity: '_1906.BevelGearMesh') -> 'Iterable[_5732.BevelGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BevelGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5732.BevelGearMeshCompoundGearWhineAnalysis))

    def results_for_conical_gear_mesh(self, design_entity: '_1910.ConicalGearMesh') -> 'Iterable[_5748.ConicalGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ConicalGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5748.ConicalGearMeshCompoundGearWhineAnalysis))

    def results_for_agma_gleason_conical_gear_mesh(self, design_entity: '_1902.AGMAGleasonConicalGearMesh') -> 'Iterable[_5720.AGMAGleasonConicalGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.AGMAGleasonConicalGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5720.AGMAGleasonConicalGearMeshCompoundGearWhineAnalysis))

    def results_for_cylindrical_gear_mesh(self, design_entity: '_1912.CylindricalGearMesh') -> 'Iterable[_5759.CylindricalGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.CylindricalGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5759.CylindricalGearMeshCompoundGearWhineAnalysis))

    def results_for_hypoid_gear_mesh(self, design_entity: '_1918.HypoidGearMesh') -> 'Iterable[_5773.HypoidGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.HypoidGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5773.HypoidGearMeshCompoundGearWhineAnalysis))

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh(self, design_entity: '_1921.KlingelnbergCycloPalloidConicalGearMesh') -> 'Iterable[_5778.KlingelnbergCycloPalloidConicalGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.KlingelnbergCycloPalloidConicalGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5778.KlingelnbergCycloPalloidConicalGearMeshCompoundGearWhineAnalysis))

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self, design_entity: '_1922.KlingelnbergCycloPalloidHypoidGearMesh') -> 'Iterable[_5781.KlingelnbergCycloPalloidHypoidGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.KlingelnbergCycloPalloidHypoidGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5781.KlingelnbergCycloPalloidHypoidGearMeshCompoundGearWhineAnalysis))

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self, design_entity: '_1923.KlingelnbergCycloPalloidSpiralBevelGearMesh') -> 'Iterable[_5784.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5784.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundGearWhineAnalysis))

    def results_for_spiral_bevel_gear_mesh(self, design_entity: '_1926.SpiralBevelGearMesh') -> 'Iterable[_5809.SpiralBevelGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.SpiralBevelGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5809.SpiralBevelGearMeshCompoundGearWhineAnalysis))

    def results_for_straight_bevel_gear_mesh(self, design_entity: '_1930.StraightBevelGearMesh') -> 'Iterable[_5818.StraightBevelGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.StraightBevelGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5818.StraightBevelGearMeshCompoundGearWhineAnalysis))

    def results_for_worm_gear_mesh(self, design_entity: '_1932.WormGearMesh') -> 'Iterable[_5833.WormGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.WormGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.WormGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_WORM_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5833.WormGearMeshCompoundGearWhineAnalysis))

    def results_for_zerol_bevel_gear_mesh(self, design_entity: '_1934.ZerolBevelGearMesh') -> 'Iterable[_5836.ZerolBevelGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ZerolBevelGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5836.ZerolBevelGearMeshCompoundGearWhineAnalysis))

    def results_for_gear_mesh(self, design_entity: '_1916.GearMesh') -> 'Iterable[_5769.GearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.GearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.GearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_GEAR_MESH](design_entity.wrapped if design_entity else None), constructor.new(_5769.GearMeshCompoundGearWhineAnalysis))

    def results_for_part_to_part_shear_coupling_connection(self, design_entity: '_1942.PartToPartShearCouplingConnection') -> 'Iterable[_5792.PartToPartShearCouplingConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.PartToPartShearCouplingConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5792.PartToPartShearCouplingConnectionCompoundGearWhineAnalysis))

    def results_for_clutch_connection(self, design_entity: '_1936.ClutchConnection') -> 'Iterable[_5737.ClutchConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ClutchConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ClutchConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CLUTCH_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5737.ClutchConnectionCompoundGearWhineAnalysis))

    def results_for_concept_coupling_connection(self, design_entity: '_1938.ConceptCouplingConnection') -> 'Iterable[_5742.ConceptCouplingConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ConceptCouplingConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5742.ConceptCouplingConnectionCompoundGearWhineAnalysis))

    def results_for_coupling_connection(self, design_entity: '_1940.CouplingConnection') -> 'Iterable[_5753.CouplingConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.CouplingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.CouplingConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_COUPLING_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5753.CouplingConnectionCompoundGearWhineAnalysis))

    def results_for_spring_damper_connection(self, design_entity: '_1944.SpringDamperConnection') -> 'Iterable[_5812.SpringDamperConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.SpringDamperConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5812.SpringDamperConnectionCompoundGearWhineAnalysis))

    def results_for_torque_converter_connection(self, design_entity: '_1946.TorqueConverterConnection') -> 'Iterable[_5827.TorqueConverterConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.TorqueConverterConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_CONNECTION](design_entity.wrapped if design_entity else None), constructor.new(_5827.TorqueConverterConnectionCompoundGearWhineAnalysis))
