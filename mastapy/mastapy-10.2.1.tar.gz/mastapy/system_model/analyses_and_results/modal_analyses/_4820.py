'''_4820.py

ModalAnalysis
'''


from mastapy.system_model.analyses_and_results.dynamic_analyses import _5893
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3058
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.modal_analyses_at_speeds_ns import _4060
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4306
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _5348
from mastapy.system_model.analyses_and_results.modal_analyses import _4823, _4821
from mastapy.system_model.analyses_and_results.analysis_cases import _6549
from mastapy._internal.python_net import python_net_import

_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'ModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ModalAnalysis',)


class ModalAnalysis(_6549.StaticLoadAnalysisCase):
    '''ModalAnalysis

    This is a mastapy class.
    '''

    TYPE = _MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def modal_analysis_results(self) -> '_5893.DynamicAnalysis':
        '''DynamicAnalysis: 'ModalAnalysisResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5893.DynamicAnalysis.TYPE not in self.wrapped.ModalAnalysisResults.__class__.__mro__:
            raise CastException('Failed to cast modal_analysis_results to DynamicAnalysis. Expected: {}.'.format(self.wrapped.ModalAnalysisResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ModalAnalysisResults.__class__)(self.wrapped.ModalAnalysisResults) if self.wrapped.ModalAnalysisResults else None

    @property
    def analysis_settings(self) -> '_4823.ModalAnalysisOptions':
        '''ModalAnalysisOptions: 'AnalysisSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_4823.ModalAnalysisOptions)(self.wrapped.AnalysisSettings) if self.wrapped.AnalysisSettings else None

    @property
    def bar_model_export(self) -> '_4821.ModalAnalysisBarModelFEExportOptions':
        '''ModalAnalysisBarModelFEExportOptions: 'BarModelExport' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_4821.ModalAnalysisBarModelFEExportOptions)(self.wrapped.BarModelExport) if self.wrapped.BarModelExport else None
