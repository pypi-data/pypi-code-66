'''_5563.py

StraightBevelGearSetSingleMeshWhineAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2132
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6242
from mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses import _5564, _5562, _5475
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_SINGLE_MESH_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.SingleMeshWhineAnalyses', 'StraightBevelGearSetSingleMeshWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearSetSingleMeshWhineAnalysis',)


class StraightBevelGearSetSingleMeshWhineAnalysis(_5475.BevelGearSetSingleMeshWhineAnalysis):
    '''StraightBevelGearSetSingleMeshWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_SINGLE_MESH_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelGearSetSingleMeshWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2132.StraightBevelGearSet':
        '''StraightBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2132.StraightBevelGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6242.StraightBevelGearSetLoadCase':
        '''StraightBevelGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6242.StraightBevelGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def straight_bevel_gears_single_mesh_whine_analysis(self) -> 'List[_5564.StraightBevelGearSingleMeshWhineAnalysis]':
        '''List[StraightBevelGearSingleMeshWhineAnalysis]: 'StraightBevelGearsSingleMeshWhineAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearsSingleMeshWhineAnalysis, constructor.new(_5564.StraightBevelGearSingleMeshWhineAnalysis))
        return value

    @property
    def straight_bevel_meshes_single_mesh_whine_analysis(self) -> 'List[_5562.StraightBevelGearMeshSingleMeshWhineAnalysis]':
        '''List[StraightBevelGearMeshSingleMeshWhineAnalysis]: 'StraightBevelMeshesSingleMeshWhineAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelMeshesSingleMeshWhineAnalysis, constructor.new(_5562.StraightBevelGearMeshSingleMeshWhineAnalysis))
        return value
