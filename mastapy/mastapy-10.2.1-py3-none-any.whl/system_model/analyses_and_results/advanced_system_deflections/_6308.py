'''_6308.py

ClutchHalfAdvancedSystemDeflection
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2159
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6120
from mastapy.system_model.analyses_and_results.system_deflections import _2273
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _6325
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'ClutchHalfAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchHalfAdvancedSystemDeflection',)


class ClutchHalfAdvancedSystemDeflection(_6325.CouplingHalfAdvancedSystemDeflection):
    '''ClutchHalfAdvancedSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _CLUTCH_HALF_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ClutchHalfAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2159.ClutchHalf':
        '''ClutchHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2159.ClutchHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6120.ClutchHalfLoadCase':
        '''ClutchHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6120.ClutchHalfLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def component_system_deflection_results(self) -> 'List[_2273.ClutchHalfSystemDeflection]':
        '''List[ClutchHalfSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentSystemDeflectionResults, constructor.new(_2273.ClutchHalfSystemDeflection))
        return value
