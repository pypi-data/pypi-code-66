'''_1877.py

ComponentMeasurer
'''


from typing import List

from mastapy._internal import constructor
from mastapy.system_model.part_model import (
    _2032, _2025, _2028, _2030,
    _2035, _2036, _2039, _2041,
    _2044, _2048, _2049, _2050,
    _2052, _2055, _2057, _2058,
    _2063, _2064
)
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.part_model.shaft_model import _2067
from mastapy.system_model.part_model.gears import (
    _2097, _2099, _2101, _2102,
    _2103, _2105, _2107, _2109,
    _2111, _2112, _2114, _2118,
    _2120, _2122, _2124, _2127,
    _2129, _2131, _2133, _2134,
    _2135, _2137
)
from mastapy.system_model.part_model.couplings import (
    _2159, _2162, _2164, _2166,
    _2168, _2169, _2175, _2177,
    _2179, _2182, _2183, _2184,
    _2186, _2188
)
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_COMPONENT_MEASURER = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'ComponentMeasurer')


__docformat__ = 'restructuredtext en'
__all__ = ('ComponentMeasurer',)


class ComponentMeasurer(_0.APIBase):
    '''ComponentMeasurer

    This is a mastapy class.
    '''

    TYPE = _COMPONENT_MEASURER

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ComponentMeasurer.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def offset_of_component(self) -> 'float':
        '''float: 'OffsetOfComponent' is the original name of this property.'''

        return self.wrapped.OffsetOfComponent

    @offset_of_component.setter
    def offset_of_component(self, value: 'float'):
        self.wrapped.OffsetOfComponent = float(value) if value else 0.0

    @property
    def component(self) -> '_2032.Component':
        '''Component: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2032.Component.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to Component. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_abstract_shaft_or_housing(self) -> '_2025.AbstractShaftOrHousing':
        '''AbstractShaftOrHousing: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2025.AbstractShaftOrHousing.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to AbstractShaftOrHousing. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_bearing(self) -> '_2028.Bearing':
        '''Bearing: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2028.Bearing.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to Bearing. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_bolt(self) -> '_2030.Bolt':
        '''Bolt: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2030.Bolt.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to Bolt. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_connector(self) -> '_2035.Connector':
        '''Connector: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2035.Connector.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to Connector. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_datum(self) -> '_2036.Datum':
        '''Datum: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2036.Datum.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to Datum. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_external_cad_model(self) -> '_2039.ExternalCADModel':
        '''ExternalCADModel: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2039.ExternalCADModel.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to ExternalCADModel. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_guide_dxf_model(self) -> '_2041.GuideDxfModel':
        '''GuideDxfModel: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2041.GuideDxfModel.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to GuideDxfModel. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_imported_fe_component(self) -> '_2044.ImportedFEComponent':
        '''ImportedFEComponent: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2044.ImportedFEComponent.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to ImportedFEComponent. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_mass_disc(self) -> '_2048.MassDisc':
        '''MassDisc: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2048.MassDisc.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to MassDisc. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_measurement_component(self) -> '_2049.MeasurementComponent':
        '''MeasurementComponent: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2049.MeasurementComponent.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to MeasurementComponent. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_mountable_component(self) -> '_2050.MountableComponent':
        '''MountableComponent: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2050.MountableComponent.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to MountableComponent. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_oil_seal(self) -> '_2052.OilSeal':
        '''OilSeal: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2052.OilSeal.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to OilSeal. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_planet_carrier(self) -> '_2055.PlanetCarrier':
        '''PlanetCarrier: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2055.PlanetCarrier.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to PlanetCarrier. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_point_load(self) -> '_2057.PointLoad':
        '''PointLoad: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2057.PointLoad.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to PointLoad. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_power_load(self) -> '_2058.PowerLoad':
        '''PowerLoad: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2058.PowerLoad.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to PowerLoad. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_unbalanced_mass(self) -> '_2063.UnbalancedMass':
        '''UnbalancedMass: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2063.UnbalancedMass.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to UnbalancedMass. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_virtual_component(self) -> '_2064.VirtualComponent':
        '''VirtualComponent: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2064.VirtualComponent.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to VirtualComponent. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_shaft(self) -> '_2067.Shaft':
        '''Shaft: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2067.Shaft.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to Shaft. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_agma_gleason_conical_gear(self) -> '_2097.AGMAGleasonConicalGear':
        '''AGMAGleasonConicalGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2097.AGMAGleasonConicalGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to AGMAGleasonConicalGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_bevel_differential_gear(self) -> '_2099.BevelDifferentialGear':
        '''BevelDifferentialGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2099.BevelDifferentialGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to BevelDifferentialGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_bevel_differential_planet_gear(self) -> '_2101.BevelDifferentialPlanetGear':
        '''BevelDifferentialPlanetGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2101.BevelDifferentialPlanetGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to BevelDifferentialPlanetGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_bevel_differential_sun_gear(self) -> '_2102.BevelDifferentialSunGear':
        '''BevelDifferentialSunGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2102.BevelDifferentialSunGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to BevelDifferentialSunGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_bevel_gear(self) -> '_2103.BevelGear':
        '''BevelGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2103.BevelGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to BevelGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_concept_gear(self) -> '_2105.ConceptGear':
        '''ConceptGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2105.ConceptGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to ConceptGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_conical_gear(self) -> '_2107.ConicalGear':
        '''ConicalGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2107.ConicalGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to ConicalGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_cylindrical_gear(self) -> '_2109.CylindricalGear':
        '''CylindricalGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2109.CylindricalGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to CylindricalGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_cylindrical_planet_gear(self) -> '_2111.CylindricalPlanetGear':
        '''CylindricalPlanetGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2111.CylindricalPlanetGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to CylindricalPlanetGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_face_gear(self) -> '_2112.FaceGear':
        '''FaceGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2112.FaceGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to FaceGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_gear(self) -> '_2114.Gear':
        '''Gear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2114.Gear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to Gear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_hypoid_gear(self) -> '_2118.HypoidGear':
        '''HypoidGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2118.HypoidGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to HypoidGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_klingelnberg_cyclo_palloid_conical_gear(self) -> '_2120.KlingelnbergCycloPalloidConicalGear':
        '''KlingelnbergCycloPalloidConicalGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2120.KlingelnbergCycloPalloidConicalGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to KlingelnbergCycloPalloidConicalGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_klingelnberg_cyclo_palloid_hypoid_gear(self) -> '_2122.KlingelnbergCycloPalloidHypoidGear':
        '''KlingelnbergCycloPalloidHypoidGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2122.KlingelnbergCycloPalloidHypoidGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to KlingelnbergCycloPalloidHypoidGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear(self) -> '_2124.KlingelnbergCycloPalloidSpiralBevelGear':
        '''KlingelnbergCycloPalloidSpiralBevelGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2124.KlingelnbergCycloPalloidSpiralBevelGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to KlingelnbergCycloPalloidSpiralBevelGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_spiral_bevel_gear(self) -> '_2127.SpiralBevelGear':
        '''SpiralBevelGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2127.SpiralBevelGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to SpiralBevelGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_straight_bevel_diff_gear(self) -> '_2129.StraightBevelDiffGear':
        '''StraightBevelDiffGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2129.StraightBevelDiffGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to StraightBevelDiffGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_straight_bevel_gear(self) -> '_2131.StraightBevelGear':
        '''StraightBevelGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2131.StraightBevelGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to StraightBevelGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_straight_bevel_planet_gear(self) -> '_2133.StraightBevelPlanetGear':
        '''StraightBevelPlanetGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2133.StraightBevelPlanetGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to StraightBevelPlanetGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_straight_bevel_sun_gear(self) -> '_2134.StraightBevelSunGear':
        '''StraightBevelSunGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2134.StraightBevelSunGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to StraightBevelSunGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_worm_gear(self) -> '_2135.WormGear':
        '''WormGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2135.WormGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to WormGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_zerol_bevel_gear(self) -> '_2137.ZerolBevelGear':
        '''ZerolBevelGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2137.ZerolBevelGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to ZerolBevelGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_clutch_half(self) -> '_2159.ClutchHalf':
        '''ClutchHalf: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2159.ClutchHalf.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to ClutchHalf. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_concept_coupling_half(self) -> '_2162.ConceptCouplingHalf':
        '''ConceptCouplingHalf: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2162.ConceptCouplingHalf.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to ConceptCouplingHalf. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_coupling_half(self) -> '_2164.CouplingHalf':
        '''CouplingHalf: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2164.CouplingHalf.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to CouplingHalf. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_cvt_pulley(self) -> '_2166.CVTPulley':
        '''CVTPulley: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2166.CVTPulley.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to CVTPulley. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_part_to_part_shear_coupling_half(self) -> '_2168.PartToPartShearCouplingHalf':
        '''PartToPartShearCouplingHalf: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2168.PartToPartShearCouplingHalf.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to PartToPartShearCouplingHalf. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_pulley(self) -> '_2169.Pulley':
        '''Pulley: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2169.Pulley.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to Pulley. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_rolling_ring(self) -> '_2175.RollingRing':
        '''RollingRing: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2175.RollingRing.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to RollingRing. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_shaft_hub_connection(self) -> '_2177.ShaftHubConnection':
        '''ShaftHubConnection: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2177.ShaftHubConnection.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to ShaftHubConnection. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_spring_damper_half(self) -> '_2179.SpringDamperHalf':
        '''SpringDamperHalf: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2179.SpringDamperHalf.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to SpringDamperHalf. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_synchroniser_half(self) -> '_2182.SynchroniserHalf':
        '''SynchroniserHalf: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2182.SynchroniserHalf.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to SynchroniserHalf. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_synchroniser_part(self) -> '_2183.SynchroniserPart':
        '''SynchroniserPart: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2183.SynchroniserPart.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to SynchroniserPart. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_synchroniser_sleeve(self) -> '_2184.SynchroniserSleeve':
        '''SynchroniserSleeve: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2184.SynchroniserSleeve.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to SynchroniserSleeve. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_torque_converter_pump(self) -> '_2186.TorqueConverterPump':
        '''TorqueConverterPump: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2186.TorqueConverterPump.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to TorqueConverterPump. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def component_of_type_torque_converter_turbine(self) -> '_2188.TorqueConverterTurbine':
        '''TorqueConverterTurbine: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2188.TorqueConverterTurbine.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to TorqueConverterTurbine. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def report_names(self) -> 'List[str]':
        '''List[str]: 'ReportNames' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ReportNames

    def output_default_report_to(self, file_path: 'str'):
        ''' 'OutputDefaultReportTo' is the original name of this method.

        Args:
            file_path (str)
        '''

        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else None)

    def get_default_report_with_encoded_images(self) -> 'str':
        ''' 'GetDefaultReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        '''

        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    def output_active_report_to(self, file_path: 'str'):
        ''' 'OutputActiveReportTo' is the original name of this method.

        Args:
            file_path (str)
        '''

        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else None)

    def output_active_report_as_text_to(self, file_path: 'str'):
        ''' 'OutputActiveReportAsTextTo' is the original name of this method.

        Args:
            file_path (str)
        '''

        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else None)

    def get_active_report_with_encoded_images(self) -> 'str':
        ''' 'GetActiveReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        '''

        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    def output_named_report_to(self, report_name: 'str', file_path: 'str'):
        ''' 'OutputNamedReportTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        '''

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(report_name if report_name else None, file_path if file_path else None)

    def output_named_report_as_masta_report(self, report_name: 'str', file_path: 'str'):
        ''' 'OutputNamedReportAsMastaReport' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        '''

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(report_name if report_name else None, file_path if file_path else None)

    def output_named_report_as_text_to(self, report_name: 'str', file_path: 'str'):
        ''' 'OutputNamedReportAsTextTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        '''

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(report_name if report_name else None, file_path if file_path else None)

    def get_named_report_with_encoded_images(self, report_name: 'str') -> 'str':
        ''' 'GetNamedReportWithEncodedImages' is the original name of this method.

        Args:
            report_name (str)

        Returns:
            str
        '''

        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(report_name if report_name else None)
        return method_result
