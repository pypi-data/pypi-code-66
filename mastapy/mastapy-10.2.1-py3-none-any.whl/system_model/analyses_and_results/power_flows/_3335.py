'''_3335.py

MeasurementComponentPowerFlow
'''


from mastapy.system_model.part_model import _2049
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6201
from mastapy.system_model.analyses_and_results.power_flows import _3382
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'MeasurementComponentPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('MeasurementComponentPowerFlow',)


class MeasurementComponentPowerFlow(_3382.VirtualComponentPowerFlow):
    '''MeasurementComponentPowerFlow

    This is a mastapy class.
    '''

    TYPE = _MEASUREMENT_COMPONENT_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MeasurementComponentPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2049.MeasurementComponent':
        '''MeasurementComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2049.MeasurementComponent)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6201.MeasurementComponentLoadCase':
        '''MeasurementComponentLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6201.MeasurementComponentLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
