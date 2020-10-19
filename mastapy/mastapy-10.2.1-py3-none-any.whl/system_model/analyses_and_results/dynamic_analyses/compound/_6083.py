'''_6083.py

UnbalancedMassCompoundDynamicAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _2063
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _5962
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6084
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'UnbalancedMassCompoundDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('UnbalancedMassCompoundDynamicAnalysis',)


class UnbalancedMassCompoundDynamicAnalysis(_6084.VirtualComponentCompoundDynamicAnalysis):
    '''UnbalancedMassCompoundDynamicAnalysis

    This is a mastapy class.
    '''

    TYPE = _UNBALANCED_MASS_COMPOUND_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'UnbalancedMassCompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2063.UnbalancedMass':
        '''UnbalancedMass: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2063.UnbalancedMass)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def load_case_analyses_ready(self) -> 'List[_5962.UnbalancedMassDynamicAnalysis]':
        '''List[UnbalancedMassDynamicAnalysis]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_5962.UnbalancedMassDynamicAnalysis))
        return value

    @property
    def component_dynamic_analysis_load_cases(self) -> 'List[_5962.UnbalancedMassDynamicAnalysis]':
        '''List[UnbalancedMassDynamicAnalysis]: 'ComponentDynamicAnalysisLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentDynamicAnalysisLoadCases, constructor.new(_5962.UnbalancedMassDynamicAnalysis))
        return value
