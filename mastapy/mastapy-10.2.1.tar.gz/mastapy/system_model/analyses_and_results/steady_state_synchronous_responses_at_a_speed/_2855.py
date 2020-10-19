'''_2855.py

RootAssemblySteadyStateSynchronousResponseAtASpeed
'''


from mastapy.system_model.part_model import _2060
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _2866, _2774
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed', 'RootAssemblySteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblySteadyStateSynchronousResponseAtASpeed',)


class RootAssemblySteadyStateSynchronousResponseAtASpeed(_2774.AssemblySteadyStateSynchronousResponseAtASpeed):
    '''RootAssemblySteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    '''

    TYPE = _ROOT_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RootAssemblySteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2060.RootAssembly':
        '''RootAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2060.RootAssembly)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def steady_state_synchronous_response_at_a_speed_inputs(self) -> '_2866.SteadyStateSynchronousResponseAtASpeed':
        '''SteadyStateSynchronousResponseAtASpeed: 'SteadyStateSynchronousResponseAtASpeedInputs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2866.SteadyStateSynchronousResponseAtASpeed)(self.wrapped.SteadyStateSynchronousResponseAtASpeedInputs) if self.wrapped.SteadyStateSynchronousResponseAtASpeedInputs else None
