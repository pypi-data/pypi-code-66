'''_3527.py

BoltedJointParametricStudyTool
'''


from typing import List

from mastapy.system_model.part_model import _2031
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6117
from mastapy.system_model.analyses_and_results.system_deflections import _2270
from mastapy.system_model.analyses_and_results.parametric_study_tools import _3617
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'BoltedJointParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltedJointParametricStudyTool',)


class BoltedJointParametricStudyTool(_3617.SpecialisedAssemblyParametricStudyTool):
    '''BoltedJointParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _BOLTED_JOINT_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BoltedJointParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2031.BoltedJoint':
        '''BoltedJoint: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2031.BoltedJoint)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6117.BoltedJointLoadCase':
        '''BoltedJointLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6117.BoltedJointLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def assembly_system_deflection_results(self) -> 'List[_2270.BoltedJointSystemDeflection]':
        '''List[BoltedJointSystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblySystemDeflectionResults, constructor.new(_2270.BoltedJointSystemDeflection))
        return value
