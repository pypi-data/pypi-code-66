'''_4109.py

SpiralBevelGearModalAnalysesAtSpeeds
'''


from mastapy.system_model.part_model.gears import _2127
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6230
from mastapy.system_model.analyses_and_results.modal_analyses_at_speeds_ns import _4029
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MODAL_ANALYSES_AT_SPEEDS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtSpeedsNS', 'SpiralBevelGearModalAnalysesAtSpeeds')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearModalAnalysesAtSpeeds',)


class SpiralBevelGearModalAnalysesAtSpeeds(_4029.BevelGearModalAnalysesAtSpeeds):
    '''SpiralBevelGearModalAnalysesAtSpeeds

    This is a mastapy class.
    '''

    TYPE = _SPIRAL_BEVEL_GEAR_MODAL_ANALYSES_AT_SPEEDS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearModalAnalysesAtSpeeds.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2127.SpiralBevelGear':
        '''SpiralBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2127.SpiralBevelGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6230.SpiralBevelGearLoadCase':
        '''SpiralBevelGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6230.SpiralBevelGearLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
