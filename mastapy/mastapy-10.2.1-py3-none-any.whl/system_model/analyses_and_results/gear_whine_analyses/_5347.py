'''_5347.py

DatumGearWhineAnalysis
'''


from mastapy.system_model.part_model import _2036
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6151
from mastapy.system_model.analyses_and_results.system_deflections import _2306
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _5325
from mastapy._internal.python_net import python_net_import

_DATUM_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'DatumGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('DatumGearWhineAnalysis',)


class DatumGearWhineAnalysis(_5325.ComponentGearWhineAnalysis):
    '''DatumGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _DATUM_GEAR_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'DatumGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2036.Datum':
        '''Datum: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2036.Datum)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6151.DatumLoadCase':
        '''DatumLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6151.DatumLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def system_deflection_results(self) -> '_2306.DatumSystemDeflection':
        '''DatumSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2306.DatumSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
