'''_5865.py

BoltedJointDynamicAnalysis
'''


from mastapy.system_model.part_model import _2031
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6117
from mastapy.system_model.analyses_and_results.dynamic_analyses import _5939
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'BoltedJointDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltedJointDynamicAnalysis',)


class BoltedJointDynamicAnalysis(_5939.SpecialisedAssemblyDynamicAnalysis):
    '''BoltedJointDynamicAnalysis

    This is a mastapy class.
    '''

    TYPE = _BOLTED_JOINT_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BoltedJointDynamicAnalysis.TYPE'):
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
