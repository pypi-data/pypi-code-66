'''_5367.py

GearMeshExcitationDetail
'''


from mastapy.system_model.analyses_and_results.system_deflections import (
    _2313, _2255, _2262, _2267,
    _2281, _2285, _2296, _2297,
    _2298, _2309, _2317, _2322,
    _2325, _2328, _2358, _2364,
    _2367, _2387, _2390
)
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import _6249
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _5324, _5301
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_EXCITATION_DETAIL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'GearMeshExcitationDetail')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshExcitationDetail',)


class GearMeshExcitationDetail(_5301.AbstractPeriodicExcitationDetail):
    '''GearMeshExcitationDetail

    This is a mastapy class.
    '''

    TYPE = _GEAR_MESH_EXCITATION_DETAIL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearMeshExcitationDetail.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_mesh(self) -> '_2313.GearMeshSystemDeflection':
        '''GearMeshSystemDeflection: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2313.GearMeshSystemDeflection.TYPE not in self.wrapped.GearMesh.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh to GearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.GearMesh.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearMesh.__class__)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    @property
    def gear_mesh_of_type_agma_gleason_conical_gear_mesh_system_deflection(self) -> '_2255.AGMAGleasonConicalGearMeshSystemDeflection':
        '''AGMAGleasonConicalGearMeshSystemDeflection: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2255.AGMAGleasonConicalGearMeshSystemDeflection.TYPE not in self.wrapped.GearMesh.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh to AGMAGleasonConicalGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.GearMesh.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearMesh.__class__)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    @property
    def gear_mesh_of_type_bevel_differential_gear_mesh_system_deflection(self) -> '_2262.BevelDifferentialGearMeshSystemDeflection':
        '''BevelDifferentialGearMeshSystemDeflection: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2262.BevelDifferentialGearMeshSystemDeflection.TYPE not in self.wrapped.GearMesh.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh to BevelDifferentialGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.GearMesh.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearMesh.__class__)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    @property
    def gear_mesh_of_type_bevel_gear_mesh_system_deflection(self) -> '_2267.BevelGearMeshSystemDeflection':
        '''BevelGearMeshSystemDeflection: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2267.BevelGearMeshSystemDeflection.TYPE not in self.wrapped.GearMesh.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh to BevelGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.GearMesh.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearMesh.__class__)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    @property
    def gear_mesh_of_type_concept_gear_mesh_system_deflection(self) -> '_2281.ConceptGearMeshSystemDeflection':
        '''ConceptGearMeshSystemDeflection: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2281.ConceptGearMeshSystemDeflection.TYPE not in self.wrapped.GearMesh.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh to ConceptGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.GearMesh.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearMesh.__class__)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    @property
    def gear_mesh_of_type_conical_gear_mesh_system_deflection(self) -> '_2285.ConicalGearMeshSystemDeflection':
        '''ConicalGearMeshSystemDeflection: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2285.ConicalGearMeshSystemDeflection.TYPE not in self.wrapped.GearMesh.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh to ConicalGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.GearMesh.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearMesh.__class__)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    @property
    def gear_mesh_of_type_cylindrical_gear_mesh_system_deflection(self) -> '_2296.CylindricalGearMeshSystemDeflection':
        '''CylindricalGearMeshSystemDeflection: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2296.CylindricalGearMeshSystemDeflection.TYPE not in self.wrapped.GearMesh.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh to CylindricalGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.GearMesh.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearMesh.__class__)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    @property
    def gear_mesh_of_type_cylindrical_gear_mesh_system_deflection_timestep(self) -> '_2297.CylindricalGearMeshSystemDeflectionTimestep':
        '''CylindricalGearMeshSystemDeflectionTimestep: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2297.CylindricalGearMeshSystemDeflectionTimestep.TYPE not in self.wrapped.GearMesh.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh to CylindricalGearMeshSystemDeflectionTimestep. Expected: {}.'.format(self.wrapped.GearMesh.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearMesh.__class__)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    @property
    def gear_mesh_of_type_cylindrical_gear_mesh_system_deflection_with_ltca_results(self) -> '_2298.CylindricalGearMeshSystemDeflectionWithLTCAResults':
        '''CylindricalGearMeshSystemDeflectionWithLTCAResults: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2298.CylindricalGearMeshSystemDeflectionWithLTCAResults.TYPE not in self.wrapped.GearMesh.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh to CylindricalGearMeshSystemDeflectionWithLTCAResults. Expected: {}.'.format(self.wrapped.GearMesh.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearMesh.__class__)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    @property
    def gear_mesh_of_type_face_gear_mesh_system_deflection(self) -> '_2309.FaceGearMeshSystemDeflection':
        '''FaceGearMeshSystemDeflection: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2309.FaceGearMeshSystemDeflection.TYPE not in self.wrapped.GearMesh.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh to FaceGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.GearMesh.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearMesh.__class__)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    @property
    def gear_mesh_of_type_hypoid_gear_mesh_system_deflection(self) -> '_2317.HypoidGearMeshSystemDeflection':
        '''HypoidGearMeshSystemDeflection: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2317.HypoidGearMeshSystemDeflection.TYPE not in self.wrapped.GearMesh.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh to HypoidGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.GearMesh.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearMesh.__class__)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    @property
    def gear_mesh_of_type_klingelnberg_cyclo_palloid_conical_gear_mesh_system_deflection(self) -> '_2322.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection':
        '''KlingelnbergCycloPalloidConicalGearMeshSystemDeflection: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2322.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection.TYPE not in self.wrapped.GearMesh.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh to KlingelnbergCycloPalloidConicalGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.GearMesh.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearMesh.__class__)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    @property
    def gear_mesh_of_type_klingelnberg_cyclo_palloid_hypoid_gear_mesh_system_deflection(self) -> '_2325.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection':
        '''KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2325.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection.TYPE not in self.wrapped.GearMesh.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh to KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.GearMesh.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearMesh.__class__)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    @property
    def gear_mesh_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_system_deflection(self) -> '_2328.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection':
        '''KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2328.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection.TYPE not in self.wrapped.GearMesh.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh to KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.GearMesh.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearMesh.__class__)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    @property
    def gear_mesh_of_type_spiral_bevel_gear_mesh_system_deflection(self) -> '_2358.SpiralBevelGearMeshSystemDeflection':
        '''SpiralBevelGearMeshSystemDeflection: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2358.SpiralBevelGearMeshSystemDeflection.TYPE not in self.wrapped.GearMesh.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh to SpiralBevelGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.GearMesh.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearMesh.__class__)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    @property
    def gear_mesh_of_type_straight_bevel_diff_gear_mesh_system_deflection(self) -> '_2364.StraightBevelDiffGearMeshSystemDeflection':
        '''StraightBevelDiffGearMeshSystemDeflection: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2364.StraightBevelDiffGearMeshSystemDeflection.TYPE not in self.wrapped.GearMesh.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh to StraightBevelDiffGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.GearMesh.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearMesh.__class__)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    @property
    def gear_mesh_of_type_straight_bevel_gear_mesh_system_deflection(self) -> '_2367.StraightBevelGearMeshSystemDeflection':
        '''StraightBevelGearMeshSystemDeflection: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2367.StraightBevelGearMeshSystemDeflection.TYPE not in self.wrapped.GearMesh.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh to StraightBevelGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.GearMesh.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearMesh.__class__)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    @property
    def gear_mesh_of_type_worm_gear_mesh_system_deflection(self) -> '_2387.WormGearMeshSystemDeflection':
        '''WormGearMeshSystemDeflection: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2387.WormGearMeshSystemDeflection.TYPE not in self.wrapped.GearMesh.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh to WormGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.GearMesh.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearMesh.__class__)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    @property
    def gear_mesh_of_type_zerol_bevel_gear_mesh_system_deflection(self) -> '_2390.ZerolBevelGearMeshSystemDeflection':
        '''ZerolBevelGearMeshSystemDeflection: 'GearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2390.ZerolBevelGearMeshSystemDeflection.TYPE not in self.wrapped.GearMesh.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh to ZerolBevelGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.GearMesh.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearMesh.__class__)(self.wrapped.GearMesh) if self.wrapped.GearMesh else None

    def get_compliance_and_force_data(self, excitation_type: '_6249.TEExcitationType') -> '_5324.ComplianceAndForceData':
        ''' 'GetComplianceAndForceData' is the original name of this method.

        Args:
            excitation_type (mastapy.system_model.analyses_and_results.static_loads.TEExcitationType)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ComplianceAndForceData
        '''

        excitation_type = conversion.mp_to_pn_enum(excitation_type)
        method_result = self.wrapped.GetComplianceAndForceData(excitation_type)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None
