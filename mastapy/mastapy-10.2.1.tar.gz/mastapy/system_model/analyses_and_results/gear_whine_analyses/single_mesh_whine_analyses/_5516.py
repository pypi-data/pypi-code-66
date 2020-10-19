'''_5516.py

HypoidGearSetSingleMeshWhineAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2119
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6187
from mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses import _5517, _5515, _5463
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_SINGLE_MESH_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.SingleMeshWhineAnalyses', 'HypoidGearSetSingleMeshWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSetSingleMeshWhineAnalysis',)


class HypoidGearSetSingleMeshWhineAnalysis(_5463.AGMAGleasonConicalGearSetSingleMeshWhineAnalysis):
    '''HypoidGearSetSingleMeshWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _HYPOID_GEAR_SET_SINGLE_MESH_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearSetSingleMeshWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2119.HypoidGearSet':
        '''HypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2119.HypoidGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6187.HypoidGearSetLoadCase':
        '''HypoidGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6187.HypoidGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def hypoid_gears_single_mesh_whine_analysis(self) -> 'List[_5517.HypoidGearSingleMeshWhineAnalysis]':
        '''List[HypoidGearSingleMeshWhineAnalysis]: 'HypoidGearsSingleMeshWhineAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearsSingleMeshWhineAnalysis, constructor.new(_5517.HypoidGearSingleMeshWhineAnalysis))
        return value

    @property
    def hypoid_meshes_single_mesh_whine_analysis(self) -> 'List[_5515.HypoidGearMeshSingleMeshWhineAnalysis]':
        '''List[HypoidGearMeshSingleMeshWhineAnalysis]: 'HypoidMeshesSingleMeshWhineAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidMeshesSingleMeshWhineAnalysis, constructor.new(_5515.HypoidGearMeshSingleMeshWhineAnalysis))
        return value
