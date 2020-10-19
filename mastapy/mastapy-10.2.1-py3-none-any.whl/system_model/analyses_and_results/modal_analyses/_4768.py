'''_4768.py

ClutchModalAnalysis
'''


from mastapy.system_model.part_model.couplings import _2158
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6121
from mastapy.system_model.analyses_and_results.system_deflections import _2274
from mastapy.system_model.analyses_and_results.modal_analyses import _4785
from mastapy._internal.python_net import python_net_import

_CLUTCH_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'ClutchModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchModalAnalysis',)


class ClutchModalAnalysis(_4785.CouplingModalAnalysis):
    '''ClutchModalAnalysis

    This is a mastapy class.
    '''

    TYPE = _CLUTCH_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ClutchModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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

    @property
    def system_deflection_results(self) -> '_2274.ClutchSystemDeflection':
        '''ClutchSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2274.ClutchSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
