'''_3734.py

RootAssemblyCompoundParametricStudyTool
'''


from mastapy.system_model.analyses_and_results.parametric_study_tools import _3597
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.load_case_groups import (
    _5281, _5280, _5282, _5285,
    _5286, _5288, _5290
)
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2448
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _3653
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'RootAssemblyCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblyCompoundParametricStudyTool',)


class RootAssemblyCompoundParametricStudyTool(_3653.AssemblyCompoundParametricStudyTool):
    '''RootAssemblyCompoundParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _ROOT_ASSEMBLY_COMPOUND_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RootAssemblyCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def parametric_analysis_options(self) -> '_3597.ParametricStudyToolOptions':
        '''ParametricStudyToolOptions: 'ParametricAnalysisOptions' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3597.ParametricStudyToolOptions)(self.wrapped.ParametricAnalysisOptions) if self.wrapped.ParametricAnalysisOptions else None

    @property
    def compound_load_case(self) -> '_5281.AbstractLoadCaseGroup':
        '''AbstractLoadCaseGroup: 'CompoundLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5281.AbstractLoadCaseGroup.TYPE not in self.wrapped.CompoundLoadCase.__class__.__mro__:
            raise CastException('Failed to cast compound_load_case to AbstractLoadCaseGroup. Expected: {}.'.format(self.wrapped.CompoundLoadCase.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CompoundLoadCase.__class__)(self.wrapped.CompoundLoadCase) if self.wrapped.CompoundLoadCase else None

    @property
    def compound_load_case_of_type_abstract_design_state_load_case_group(self) -> '_5280.AbstractDesignStateLoadCaseGroup':
        '''AbstractDesignStateLoadCaseGroup: 'CompoundLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5280.AbstractDesignStateLoadCaseGroup.TYPE not in self.wrapped.CompoundLoadCase.__class__.__mro__:
            raise CastException('Failed to cast compound_load_case to AbstractDesignStateLoadCaseGroup. Expected: {}.'.format(self.wrapped.CompoundLoadCase.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CompoundLoadCase.__class__)(self.wrapped.CompoundLoadCase) if self.wrapped.CompoundLoadCase else None

    @property
    def compound_load_case_of_type_abstract_static_load_case_group(self) -> '_5282.AbstractStaticLoadCaseGroup':
        '''AbstractStaticLoadCaseGroup: 'CompoundLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5282.AbstractStaticLoadCaseGroup.TYPE not in self.wrapped.CompoundLoadCase.__class__.__mro__:
            raise CastException('Failed to cast compound_load_case to AbstractStaticLoadCaseGroup. Expected: {}.'.format(self.wrapped.CompoundLoadCase.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CompoundLoadCase.__class__)(self.wrapped.CompoundLoadCase) if self.wrapped.CompoundLoadCase else None

    @property
    def compound_load_case_of_type_design_state(self) -> '_5285.DesignState':
        '''DesignState: 'CompoundLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5285.DesignState.TYPE not in self.wrapped.CompoundLoadCase.__class__.__mro__:
            raise CastException('Failed to cast compound_load_case to DesignState. Expected: {}.'.format(self.wrapped.CompoundLoadCase.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CompoundLoadCase.__class__)(self.wrapped.CompoundLoadCase) if self.wrapped.CompoundLoadCase else None

    @property
    def compound_load_case_of_type_duty_cycle(self) -> '_5286.DutyCycle':
        '''DutyCycle: 'CompoundLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5286.DutyCycle.TYPE not in self.wrapped.CompoundLoadCase.__class__.__mro__:
            raise CastException('Failed to cast compound_load_case to DutyCycle. Expected: {}.'.format(self.wrapped.CompoundLoadCase.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CompoundLoadCase.__class__)(self.wrapped.CompoundLoadCase) if self.wrapped.CompoundLoadCase else None

    @property
    def compound_load_case_of_type_group_of_time_series_load_cases(self) -> '_5288.GroupOfTimeSeriesLoadCases':
        '''GroupOfTimeSeriesLoadCases: 'CompoundLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5288.GroupOfTimeSeriesLoadCases.TYPE not in self.wrapped.CompoundLoadCase.__class__.__mro__:
            raise CastException('Failed to cast compound_load_case to GroupOfTimeSeriesLoadCases. Expected: {}.'.format(self.wrapped.CompoundLoadCase.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CompoundLoadCase.__class__)(self.wrapped.CompoundLoadCase) if self.wrapped.CompoundLoadCase else None

    @property
    def compound_load_case_of_type_sub_group_in_single_design_state(self) -> '_5290.SubGroupInSingleDesignState':
        '''SubGroupInSingleDesignState: 'CompoundLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5290.SubGroupInSingleDesignState.TYPE not in self.wrapped.CompoundLoadCase.__class__.__mro__:
            raise CastException('Failed to cast compound_load_case to SubGroupInSingleDesignState. Expected: {}.'.format(self.wrapped.CompoundLoadCase.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CompoundLoadCase.__class__)(self.wrapped.CompoundLoadCase) if self.wrapped.CompoundLoadCase else None

    @property
    def root_assembly_duty_cycle_results(self) -> '_2448.DutyCycleEfficiencyResults':
        '''DutyCycleEfficiencyResults: 'RootAssemblyDutyCycleResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2448.DutyCycleEfficiencyResults)(self.wrapped.RootAssemblyDutyCycleResults) if self.wrapped.RootAssemblyDutyCycleResults else None
