'''_3285.py

ClutchPowerFlow
'''


from mastapy.system_model.analyses_and_results.power_flows import _3283, _3301
from mastapy._internal import constructor
from mastapy.system_model.part_model.couplings import _2158
from mastapy.system_model.analyses_and_results.static_loads import _6121
from mastapy._internal.python_net import python_net_import

_CLUTCH_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'ClutchPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchPowerFlow',)


class ClutchPowerFlow(_3301.CouplingPowerFlow):
    '''ClutchPowerFlow

    This is a mastapy class.
    '''

    TYPE = _CLUTCH_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ClutchPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def clutch_connection(self) -> '_3283.ClutchConnectionPowerFlow':
        '''ClutchConnectionPowerFlow: 'ClutchConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3283.ClutchConnectionPowerFlow)(self.wrapped.ClutchConnection) if self.wrapped.ClutchConnection else None

    @property
    def assembly_design(self) -> '_2158.Clutch':
        '''Clutch: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2158.Clutch)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6121.ClutchLoadCase':
        '''ClutchLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6121.ClutchLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None
