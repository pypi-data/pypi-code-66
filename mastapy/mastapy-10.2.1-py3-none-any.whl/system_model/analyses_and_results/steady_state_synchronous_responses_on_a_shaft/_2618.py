'''_2618.py

SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft
'''


from typing import List

from mastapy.system_model.part_model.gears import _2128
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6232
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _2619, _2617, _2541
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft', 'SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft',)


class SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft(_2541.BevelGearSetSteadyStateSynchronousResponseOnAShaft):
    '''SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    '''

    TYPE = _SPIRAL_BEVEL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2128.SpiralBevelGearSet':
        '''SpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2128.SpiralBevelGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6232.SpiralBevelGearSetLoadCase':
        '''SpiralBevelGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6232.SpiralBevelGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def spiral_bevel_gears_steady_state_synchronous_response_on_a_shaft(self) -> 'List[_2619.SpiralBevelGearSteadyStateSynchronousResponseOnAShaft]':
        '''List[SpiralBevelGearSteadyStateSynchronousResponseOnAShaft]: 'SpiralBevelGearsSteadyStateSynchronousResponseOnAShaft' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearsSteadyStateSynchronousResponseOnAShaft, constructor.new(_2619.SpiralBevelGearSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def spiral_bevel_meshes_steady_state_synchronous_response_on_a_shaft(self) -> 'List[_2617.SpiralBevelGearMeshSteadyStateSynchronousResponseOnAShaft]':
        '''List[SpiralBevelGearMeshSteadyStateSynchronousResponseOnAShaft]: 'SpiralBevelMeshesSteadyStateSynchronousResponseOnAShaft' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelMeshesSteadyStateSynchronousResponseOnAShaft, constructor.new(_2617.SpiralBevelGearMeshSteadyStateSynchronousResponseOnAShaft))
        return value
