'''_5403.py

PlanetCarrierGearWhineAnalysis
'''


from mastapy.system_model.part_model import _2055
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6214
from mastapy.system_model.analyses_and_results.system_deflections import _2344
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _5394
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'PlanetCarrierGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetCarrierGearWhineAnalysis',)


class PlanetCarrierGearWhineAnalysis(_5394.MountableComponentGearWhineAnalysis):
    '''PlanetCarrierGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _PLANET_CARRIER_GEAR_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PlanetCarrierGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2055.PlanetCarrier':
        '''PlanetCarrier: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2055.PlanetCarrier)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6214.PlanetCarrierLoadCase':
        '''PlanetCarrierLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6214.PlanetCarrierLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def system_deflection_results(self) -> '_2344.PlanetCarrierSystemDeflection':
        '''PlanetCarrierSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2344.PlanetCarrierSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
