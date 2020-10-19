'''_5404.py

PointLoadGearWhineAnalysis
'''


from mastapy.system_model.part_model import _2057
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6217
from mastapy.system_model.analyses_and_results.system_deflections import _2345
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _5441
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'PointLoadGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PointLoadGearWhineAnalysis',)


class PointLoadGearWhineAnalysis(_5441.VirtualComponentGearWhineAnalysis):
    '''PointLoadGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _POINT_LOAD_GEAR_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PointLoadGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2057.PointLoad':
        '''PointLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2057.PointLoad)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6217.PointLoadLoadCase':
        '''PointLoadLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6217.PointLoadLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def system_deflection_results(self) -> '_2345.PointLoadSystemDeflection':
        '''PointLoadSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2345.PointLoadSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
