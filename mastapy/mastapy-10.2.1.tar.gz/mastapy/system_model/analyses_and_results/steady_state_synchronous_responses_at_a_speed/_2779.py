'''_2779.py

BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed
'''


from typing import List

from mastapy.system_model.part_model.gears import _2100
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6111
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _2780, _2778, _2784
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed', 'BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed',)


class BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed(_2784.BevelGearSetSteadyStateSynchronousResponseAtASpeed):
    '''BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    '''

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2100.BevelDifferentialGearSet':
        '''BevelDifferentialGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2100.BevelDifferentialGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6111.BevelDifferentialGearSetLoadCase':
        '''BevelDifferentialGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6111.BevelDifferentialGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def bevel_differential_gears_steady_state_synchronous_response_at_a_speed(self) -> 'List[_2780.BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed]':
        '''List[BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed]: 'BevelDifferentialGearsSteadyStateSynchronousResponseAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearsSteadyStateSynchronousResponseAtASpeed, constructor.new(_2780.BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed))
        return value

    @property
    def bevel_differential_meshes_steady_state_synchronous_response_at_a_speed(self) -> 'List[_2778.BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed]':
        '''List[BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed]: 'BevelDifferentialMeshesSteadyStateSynchronousResponseAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialMeshesSteadyStateSynchronousResponseAtASpeed, constructor.new(_2778.BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed))
        return value
