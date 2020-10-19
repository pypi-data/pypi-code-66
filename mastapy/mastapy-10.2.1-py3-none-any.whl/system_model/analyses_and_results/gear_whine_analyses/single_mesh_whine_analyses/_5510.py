'''_5510.py

FlexiblePinAssemblySingleMeshWhineAnalysis
'''


from mastapy.system_model.part_model import _2040
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6168
from mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses import _5552
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_SINGLE_MESH_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.SingleMeshWhineAnalyses', 'FlexiblePinAssemblySingleMeshWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FlexiblePinAssemblySingleMeshWhineAnalysis',)


class FlexiblePinAssemblySingleMeshWhineAnalysis(_5552.SpecialisedAssemblySingleMeshWhineAnalysis):
    '''FlexiblePinAssemblySingleMeshWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_SINGLE_MESH_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FlexiblePinAssemblySingleMeshWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2040.FlexiblePinAssembly':
        '''FlexiblePinAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2040.FlexiblePinAssembly)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6168.FlexiblePinAssemblyLoadCase':
        '''FlexiblePinAssemblyLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6168.FlexiblePinAssemblyLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None
