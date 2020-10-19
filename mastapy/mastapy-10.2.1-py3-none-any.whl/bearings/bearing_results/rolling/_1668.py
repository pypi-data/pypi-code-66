'''_1668.py

LoadedFourPointContactBallBearingRow
'''


from typing import List

from mastapy.bearings.bearing_results.rolling import _1667, _1666, _1653
from mastapy._internal import constructor, conversion
from mastapy._internal.python_net import python_net_import

_LOADED_FOUR_POINT_CONTACT_BALL_BEARING_ROW = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedFourPointContactBallBearingRow')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedFourPointContactBallBearingRow',)


class LoadedFourPointContactBallBearingRow(_1653.LoadedBallBearingRow):
    '''LoadedFourPointContactBallBearingRow

    This is a mastapy class.
    '''

    TYPE = _LOADED_FOUR_POINT_CONTACT_BALL_BEARING_ROW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'LoadedFourPointContactBallBearingRow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def loaded_bearing(self) -> '_1667.LoadedFourPointContactBallBearingResults':
        '''LoadedFourPointContactBallBearingResults: 'LoadedBearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1667.LoadedFourPointContactBallBearingResults)(self.wrapped.LoadedBearing) if self.wrapped.LoadedBearing else None

    @property
    def race_results(self) -> 'List[_1666.LoadedFourPointContactBallBearingRaceResults]':
        '''List[LoadedFourPointContactBallBearingRaceResults]: 'RaceResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RaceResults, constructor.new(_1666.LoadedFourPointContactBallBearingRaceResults))
        return value
