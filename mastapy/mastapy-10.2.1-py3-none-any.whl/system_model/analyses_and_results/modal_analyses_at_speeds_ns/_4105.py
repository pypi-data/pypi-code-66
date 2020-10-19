'''_4105.py

ShaftModalAnalysesAtSpeeds
'''


from typing import List

from mastapy.system_model.part_model.shaft_model import _2067
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6226
from mastapy.system_model.analyses_and_results.modal_analyses_at_speeds_ns import _4015
from mastapy._internal.python_net import python_net_import

_SHAFT_MODAL_ANALYSES_AT_SPEEDS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtSpeedsNS', 'ShaftModalAnalysesAtSpeeds')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftModalAnalysesAtSpeeds',)


class ShaftModalAnalysesAtSpeeds(_4015.AbstractShaftOrHousingModalAnalysesAtSpeeds):
    '''ShaftModalAnalysesAtSpeeds

    This is a mastapy class.
    '''

    TYPE = _SHAFT_MODAL_ANALYSES_AT_SPEEDS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ShaftModalAnalysesAtSpeeds.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2067.Shaft':
        '''Shaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2067.Shaft)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6226.ShaftLoadCase':
        '''ShaftLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6226.ShaftLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def planetaries(self) -> 'List[ShaftModalAnalysesAtSpeeds]':
        '''List[ShaftModalAnalysesAtSpeeds]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(ShaftModalAnalysesAtSpeeds))
        return value
