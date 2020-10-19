'''_3835.py

KlingelnbergCycloPalloidHypoidGearSetModalAnalysesAtStiffnesses
'''


from typing import List

from mastapy.system_model.part_model.gears import _2123
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6196
from mastapy.system_model.analyses_and_results.modal_analyses_at_stiffnesses_ns import _3834, _3833, _3832
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_MODAL_ANALYSES_AT_STIFFNESSES = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtStiffnessesNS', 'KlingelnbergCycloPalloidHypoidGearSetModalAnalysesAtStiffnesses')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearSetModalAnalysesAtStiffnesses',)


class KlingelnbergCycloPalloidHypoidGearSetModalAnalysesAtStiffnesses(_3832.KlingelnbergCycloPalloidConicalGearSetModalAnalysesAtStiffnesses):
    '''KlingelnbergCycloPalloidHypoidGearSetModalAnalysesAtStiffnesses

    This is a mastapy class.
    '''

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_MODAL_ANALYSES_AT_STIFFNESSES

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearSetModalAnalysesAtStiffnesses.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2123.KlingelnbergCycloPalloidHypoidGearSet':
        '''KlingelnbergCycloPalloidHypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2123.KlingelnbergCycloPalloidHypoidGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6196.KlingelnbergCycloPalloidHypoidGearSetLoadCase':
        '''KlingelnbergCycloPalloidHypoidGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6196.KlingelnbergCycloPalloidHypoidGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_modal_analyses_at_stiffnesses(self) -> 'List[_3834.KlingelnbergCycloPalloidHypoidGearModalAnalysesAtStiffnesses]':
        '''List[KlingelnbergCycloPalloidHypoidGearModalAnalysesAtStiffnesses]: 'KlingelnbergCycloPalloidHypoidGearsModalAnalysesAtStiffnesses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearsModalAnalysesAtStiffnesses, constructor.new(_3834.KlingelnbergCycloPalloidHypoidGearModalAnalysesAtStiffnesses))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_modal_analyses_at_stiffnesses(self) -> 'List[_3833.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysesAtStiffnesses]':
        '''List[KlingelnbergCycloPalloidHypoidGearMeshModalAnalysesAtStiffnesses]: 'KlingelnbergCycloPalloidHypoidMeshesModalAnalysesAtStiffnesses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidMeshesModalAnalysesAtStiffnesses, constructor.new(_3833.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysesAtStiffnesses))
        return value
