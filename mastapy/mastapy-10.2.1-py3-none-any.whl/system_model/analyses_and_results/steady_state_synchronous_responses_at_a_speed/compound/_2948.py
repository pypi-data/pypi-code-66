'''_2948.py

HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed
'''


from typing import List

from mastapy.system_model.part_model.gears import _2119
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _2946, _2947, _2895
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _2825
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound', 'HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed',)


class HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed(_2895.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed):
    '''HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    '''

    TYPE = _HYPOID_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed.TYPE'):
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
    def hypoid_gears_compound_steady_state_synchronous_response_at_a_speed(self) -> 'List[_2946.HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed]':
        '''List[HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed]: 'HypoidGearsCompoundSteadyStateSynchronousResponseAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearsCompoundSteadyStateSynchronousResponseAtASpeed, constructor.new(_2946.HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed))
        return value

    @property
    def hypoid_meshes_compound_steady_state_synchronous_response_at_a_speed(self) -> 'List[_2947.HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed]':
        '''List[HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed]: 'HypoidMeshesCompoundSteadyStateSynchronousResponseAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidMeshesCompoundSteadyStateSynchronousResponseAtASpeed, constructor.new(_2947.HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed))
        return value

    @property
    def load_case_analyses_ready(self) -> 'List[_2825.HypoidGearSetSteadyStateSynchronousResponseAtASpeed]':
        '''List[HypoidGearSetSteadyStateSynchronousResponseAtASpeed]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_2825.HypoidGearSetSteadyStateSynchronousResponseAtASpeed))
        return value

    @property
    def assembly_steady_state_synchronous_response_at_a_speed_load_cases(self) -> 'List[_2825.HypoidGearSetSteadyStateSynchronousResponseAtASpeed]':
        '''List[HypoidGearSetSteadyStateSynchronousResponseAtASpeed]: 'AssemblySteadyStateSynchronousResponseAtASpeedLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblySteadyStateSynchronousResponseAtASpeedLoadCases, constructor.new(_2825.HypoidGearSetSteadyStateSynchronousResponseAtASpeed))
        return value
