'''_4364.py

StraightBevelGearSetModalAnalysisAtAStiffness
'''


from typing import List

from mastapy.system_model.part_model.gears import _2132
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6242
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4363, _4362, _4276
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'StraightBevelGearSetModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearSetModalAnalysisAtAStiffness',)


class StraightBevelGearSetModalAnalysisAtAStiffness(_4276.BevelGearSetModalAnalysisAtAStiffness):
    '''StraightBevelGearSetModalAnalysisAtAStiffness

    This is a mastapy class.
    '''

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelGearSetModalAnalysisAtAStiffness.TYPE'):
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
    def straight_bevel_gears_modal_analysis_at_a_stiffness(self) -> 'List[_4363.StraightBevelGearModalAnalysisAtAStiffness]':
        '''List[StraightBevelGearModalAnalysisAtAStiffness]: 'StraightBevelGearsModalAnalysisAtAStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearsModalAnalysisAtAStiffness, constructor.new(_4363.StraightBevelGearModalAnalysisAtAStiffness))
        return value

    @property
    def straight_bevel_meshes_modal_analysis_at_a_stiffness(self) -> 'List[_4362.StraightBevelGearMeshModalAnalysisAtAStiffness]':
        '''List[StraightBevelGearMeshModalAnalysisAtAStiffness]: 'StraightBevelMeshesModalAnalysisAtAStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelMeshesModalAnalysisAtAStiffness, constructor.new(_4362.StraightBevelGearMeshModalAnalysisAtAStiffness))
        return value
