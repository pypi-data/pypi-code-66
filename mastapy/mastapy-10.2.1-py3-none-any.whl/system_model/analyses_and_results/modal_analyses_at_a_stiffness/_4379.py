'''_4379.py

WormGearSetModalAnalysisAtAStiffness
'''


from typing import List

from mastapy.system_model.part_model.gears import _2136
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6263
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4378, _4377, _4314
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'WormGearSetModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetModalAnalysisAtAStiffness',)


class WormGearSetModalAnalysisAtAStiffness(_4314.GearSetModalAnalysisAtAStiffness):
    '''WormGearSetModalAnalysisAtAStiffness

    This is a mastapy class.
    '''

    TYPE = _WORM_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearSetModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2136.WormGearSet':
        '''WormGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2136.WormGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6263.WormGearSetLoadCase':
        '''WormGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6263.WormGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def worm_gears_modal_analysis_at_a_stiffness(self) -> 'List[_4378.WormGearModalAnalysisAtAStiffness]':
        '''List[WormGearModalAnalysisAtAStiffness]: 'WormGearsModalAnalysisAtAStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearsModalAnalysisAtAStiffness, constructor.new(_4378.WormGearModalAnalysisAtAStiffness))
        return value

    @property
    def worm_meshes_modal_analysis_at_a_stiffness(self) -> 'List[_4377.WormGearMeshModalAnalysisAtAStiffness]':
        '''List[WormGearMeshModalAnalysisAtAStiffness]: 'WormMeshesModalAnalysisAtAStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormMeshesModalAnalysisAtAStiffness, constructor.new(_4377.WormGearMeshModalAnalysisAtAStiffness))
        return value
