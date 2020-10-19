'''_5640.py

HypoidGearSetCompoundSingleMeshWhineAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2119
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound import _5638, _5639, _5587
from mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses import _5516
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_COMPOUND_SINGLE_MESH_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.SingleMeshWhineAnalyses.Compound', 'HypoidGearSetCompoundSingleMeshWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSetCompoundSingleMeshWhineAnalysis',)


class HypoidGearSetCompoundSingleMeshWhineAnalysis(_5587.AGMAGleasonConicalGearSetCompoundSingleMeshWhineAnalysis):
    '''HypoidGearSetCompoundSingleMeshWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _HYPOID_GEAR_SET_COMPOUND_SINGLE_MESH_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearSetCompoundSingleMeshWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2119.HypoidGearSet':
        '''HypoidGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2119.HypoidGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def assembly_design(self) -> '_2119.HypoidGearSet':
        '''HypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2119.HypoidGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def hypoid_gears_compound_single_mesh_whine_analysis(self) -> 'List[_5638.HypoidGearCompoundSingleMeshWhineAnalysis]':
        '''List[HypoidGearCompoundSingleMeshWhineAnalysis]: 'HypoidGearsCompoundSingleMeshWhineAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearsCompoundSingleMeshWhineAnalysis, constructor.new(_5638.HypoidGearCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def hypoid_meshes_compound_single_mesh_whine_analysis(self) -> 'List[_5639.HypoidGearMeshCompoundSingleMeshWhineAnalysis]':
        '''List[HypoidGearMeshCompoundSingleMeshWhineAnalysis]: 'HypoidMeshesCompoundSingleMeshWhineAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidMeshesCompoundSingleMeshWhineAnalysis, constructor.new(_5639.HypoidGearMeshCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def load_case_analyses_ready(self) -> 'List[_5516.HypoidGearSetSingleMeshWhineAnalysis]':
        '''List[HypoidGearSetSingleMeshWhineAnalysis]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_5516.HypoidGearSetSingleMeshWhineAnalysis))
        return value

    @property
    def assembly_single_mesh_whine_analysis_load_cases(self) -> 'List[_5516.HypoidGearSetSingleMeshWhineAnalysis]':
        '''List[HypoidGearSetSingleMeshWhineAnalysis]: 'AssemblySingleMeshWhineAnalysisLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblySingleMeshWhineAnalysisLoadCases, constructor.new(_5516.HypoidGearSetSingleMeshWhineAnalysis))
        return value
