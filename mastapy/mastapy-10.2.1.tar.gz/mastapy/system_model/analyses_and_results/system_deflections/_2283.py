'''_2283.py

ConceptGearSystemDeflection
'''


from mastapy.system_model.part_model.gears import _2105
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6127
from mastapy.system_model.analyses_and_results.power_flows import _3292
from mastapy.gears.rating.concept import _335
from mastapy.system_model.analyses_and_results.system_deflections import _2315
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'ConceptGearSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearSystemDeflection',)


class ConceptGearSystemDeflection(_2315.GearSystemDeflection):
    '''ConceptGearSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_GEAR_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptGearSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2105.ConceptGear':
        '''ConceptGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2105.ConceptGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6127.ConceptGearLoadCase':
        '''ConceptGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6127.ConceptGearLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def power_flow_results(self) -> '_3292.ConceptGearPowerFlow':
        '''ConceptGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3292.ConceptGearPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults else None

    @property
    def component_detailed_analysis(self) -> '_335.ConceptGearRating':
        '''ConceptGearRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_335.ConceptGearRating)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None
