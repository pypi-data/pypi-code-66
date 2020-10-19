'''_3096.py

RollingRingAssemblySteadyStateSynchronousResponse
'''


from mastapy.system_model.part_model.couplings import _2176
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6221
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3103
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'RollingRingAssemblySteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('RollingRingAssemblySteadyStateSynchronousResponse',)


class RollingRingAssemblySteadyStateSynchronousResponse(_3103.SpecialisedAssemblySteadyStateSynchronousResponse):
    '''RollingRingAssemblySteadyStateSynchronousResponse

    This is a mastapy class.
    '''

    TYPE = _ROLLING_RING_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RollingRingAssemblySteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2176.RollingRingAssembly':
        '''RollingRingAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2176.RollingRingAssembly)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6221.RollingRingAssemblyLoadCase':
        '''RollingRingAssemblyLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6221.RollingRingAssemblyLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None
