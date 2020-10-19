'''_5380.py

HypoidGearSetGearWhineAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2119
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6187
from mastapy.system_model.analyses_and_results.system_deflections import _2318
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _5378, _5379, _5305
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'HypoidGearSetGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSetGearWhineAnalysis',)


class HypoidGearSetGearWhineAnalysis(_5305.AGMAGleasonConicalGearSetGearWhineAnalysis):
    '''HypoidGearSetGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _HYPOID_GEAR_SET_GEAR_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearSetGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2119.HypoidGearSet':
        '''HypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2119.HypoidGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6187.HypoidGearSetLoadCase':
        '''HypoidGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6187.HypoidGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def system_deflection_results(self) -> '_2318.HypoidGearSetSystemDeflection':
        '''HypoidGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2318.HypoidGearSetSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None

    @property
    def gears_gear_whine_analysis(self) -> 'List[_5378.HypoidGearGearWhineAnalysis]':
        '''List[HypoidGearGearWhineAnalysis]: 'GearsGearWhineAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.GearsGearWhineAnalysis, constructor.new(_5378.HypoidGearGearWhineAnalysis))
        return value

    @property
    def hypoid_gears_gear_whine_analysis(self) -> 'List[_5378.HypoidGearGearWhineAnalysis]':
        '''List[HypoidGearGearWhineAnalysis]: 'HypoidGearsGearWhineAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearsGearWhineAnalysis, constructor.new(_5378.HypoidGearGearWhineAnalysis))
        return value

    @property
    def meshes_gear_whine_analysis(self) -> 'List[_5379.HypoidGearMeshGearWhineAnalysis]':
        '''List[HypoidGearMeshGearWhineAnalysis]: 'MeshesGearWhineAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeshesGearWhineAnalysis, constructor.new(_5379.HypoidGearMeshGearWhineAnalysis))
        return value

    @property
    def hypoid_meshes_gear_whine_analysis(self) -> 'List[_5379.HypoidGearMeshGearWhineAnalysis]':
        '''List[HypoidGearMeshGearWhineAnalysis]: 'HypoidMeshesGearWhineAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidMeshesGearWhineAnalysis, constructor.new(_5379.HypoidGearMeshGearWhineAnalysis))
        return value
