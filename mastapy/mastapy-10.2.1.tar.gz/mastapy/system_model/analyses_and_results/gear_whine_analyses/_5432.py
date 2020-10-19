'''_5432.py

SynchroniserHalfGearWhineAnalysis
'''


from mastapy.system_model.part_model.couplings import _2182
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6245
from mastapy.system_model.analyses_and_results.system_deflections import _2372
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _5433
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'SynchroniserHalfGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserHalfGearWhineAnalysis',)


class SynchroniserHalfGearWhineAnalysis(_5433.SynchroniserPartGearWhineAnalysis):
    '''SynchroniserHalfGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _SYNCHRONISER_HALF_GEAR_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SynchroniserHalfGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2182.SynchroniserHalf':
        '''SynchroniserHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2182.SynchroniserHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6245.SynchroniserHalfLoadCase':
        '''SynchroniserHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6245.SynchroniserHalfLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def system_deflection_results(self) -> '_2372.SynchroniserHalfSystemDeflection':
        '''SynchroniserHalfSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2372.SynchroniserHalfSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
