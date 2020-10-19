'''_5524.py

KlingelnbergCycloPalloidHypoidGearSetSingleMeshWhineAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2123
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6196
from mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses import _5525, _5523, _5521
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_SINGLE_MESH_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.SingleMeshWhineAnalyses', 'KlingelnbergCycloPalloidHypoidGearSetSingleMeshWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearSetSingleMeshWhineAnalysis',)


class KlingelnbergCycloPalloidHypoidGearSetSingleMeshWhineAnalysis(_5521.KlingelnbergCycloPalloidConicalGearSetSingleMeshWhineAnalysis):
    '''KlingelnbergCycloPalloidHypoidGearSetSingleMeshWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_SINGLE_MESH_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearSetSingleMeshWhineAnalysis.TYPE'):
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
    def klingelnberg_cyclo_palloid_hypoid_gears_single_mesh_whine_analysis(self) -> 'List[_5525.KlingelnbergCycloPalloidHypoidGearSingleMeshWhineAnalysis]':
        '''List[KlingelnbergCycloPalloidHypoidGearSingleMeshWhineAnalysis]: 'KlingelnbergCycloPalloidHypoidGearsSingleMeshWhineAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearsSingleMeshWhineAnalysis, constructor.new(_5525.KlingelnbergCycloPalloidHypoidGearSingleMeshWhineAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_single_mesh_whine_analysis(self) -> 'List[_5523.KlingelnbergCycloPalloidHypoidGearMeshSingleMeshWhineAnalysis]':
        '''List[KlingelnbergCycloPalloidHypoidGearMeshSingleMeshWhineAnalysis]: 'KlingelnbergCycloPalloidHypoidMeshesSingleMeshWhineAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidMeshesSingleMeshWhineAnalysis, constructor.new(_5523.KlingelnbergCycloPalloidHypoidGearMeshSingleMeshWhineAnalysis))
        return value
