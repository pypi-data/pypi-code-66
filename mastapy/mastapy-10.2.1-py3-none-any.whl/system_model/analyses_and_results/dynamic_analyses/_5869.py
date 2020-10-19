'''_5869.py

CoaxialConnectionDynamicAnalysis
'''


from mastapy.system_model.connections_and_sockets import _1875
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6122
from mastapy.system_model.analyses_and_results.dynamic_analyses import _5938
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'CoaxialConnectionDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CoaxialConnectionDynamicAnalysis',)


class CoaxialConnectionDynamicAnalysis(_5938.ShaftToMountableComponentConnectionDynamicAnalysis):
    '''CoaxialConnectionDynamicAnalysis

    This is a mastapy class.
    '''

    TYPE = _COAXIAL_CONNECTION_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CoaxialConnectionDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_1875.CoaxialConnection':
        '''CoaxialConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1875.CoaxialConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_load_case(self) -> '_6122.CoaxialConnectionLoadCase':
        '''CoaxialConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6122.CoaxialConnectionLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase else None
