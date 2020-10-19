# -*- coding: utf-8 -*-
import logging
import pandas as pd
import numpy as np
from seasonal_behavior_deviation.result import SBDResult

from .util import create_sliding_windows, normalize_column, df_euclidean_distance, adjust_normal_behavior_to_trend, \
    extract_normal_behavior, detrend_series

__author__ = "Jannik Frauendorf"
__copyright__ = "Jannik Frauendorf"
__license__ = "mit"

_logger = logging.getLogger(__name__)

# ----------------------------------------------------------------------
# Class containing the logic behind the Seasonal Behavior Deviation algorithm.
# ----------------------------------------------------------------------


class SeasonalBehaviorDeviation(object):
    def __init__(self, data: list, season_length: int, window_size=1, detrend=True) -> None:
        """
        :param data: list containing the time series with evenly distributed values (i.e., no gaps allowed)
        :param season_length: an integer specifying the number of rows that make up one season
        :param window_size:  This parameter specifies how fine SBD should narrow down the discords.
            With smaller window_size, the anomaly_score vector becomes spikier, and the single anomalies become clear.
            By choosing higher values, the score curve becomes smoother. Moreover, with greater window_sizes, multiple close
            anomalies can be summarized to one larger anomaly.
        :param detrend: flag whether the original data should be de-trended or not

        """

        self.detrend = detrend
        if not isinstance(data, list):
            raise TypeError('Wrong data format. Was expecting a list, got %s.' % type(data))

        self.data = data
        self.season_length = season_length
        self.window_size = window_size
        self.__result = SBDResult(data)

    def detect(self):
        """
        Assigns an anomaly score to each data point of a list by using the Seasonal Behavior Deviation algorithm.
        """

        value_column_name = "values"
        previous_index_name = "original_index"
        previous_index = list(range(0, len(self.data)))
        season_length = self.season_length
        window_size = self.window_size

        df = pd.DataFrame({value_column_name: self.data,
                           previous_index_name: previous_index})

        # normalize original data
        df = normalize_column(df=df, column_name=value_column_name)

        # compute season steps: position index within one season
        # ranging from 0 to season_length-1
        season_steps = df.index % season_length

        if self.detrend:
            trend_diff, detrended_values = detrend_series(df[value_column_name], season_length)
        else:
            # original values as detrended
            detrended_values = df[value_column_name].copy(deep=True)
            trend_diff = None

        # normal_behavior is a series of length season_length
        normal_behavior = extract_normal_behavior(detrended_values, season_steps)
        normal_behavior = normal_behavior.rename("normal_behavior").rename_axis("season_step")

        df.loc[:, 'season_step'] = season_steps
        # join normal behavior with original data
        df = pd.merge(df, normal_behavior, how='inner', on='season_step')

        # the join operation removes the order of the rows => reset the ordering to the original index column
        df = df.set_index(previous_index_name, drop=False)

        # sort by index
        df = df.sort_index()

        if self.detrend:
            # adjust the normal behavior based on the extracted trend
            df.loc[:, "normal_behavior"] = adjust_normal_behavior_to_trend(df.loc[:, "normal_behavior"], trend_diff)

        # generate sliding window data frame over the normal behavior vector and the value vector (both normalized)
        normal_behavior_windows = create_sliding_windows(df.loc[:, 'normal_behavior'], window_size)
        series_behavior_windows = create_sliding_windows(df.loc[:, value_column_name], window_size)

        # compute scores as row-wise Euclidean Distance between normal behavior and the actual values
        scores = df_euclidean_distance(normal_behavior_windows, series_behavior_windows)

        # move anomaly scores to center of window
        first_part = int((window_size - 1) / 2)
        second_part = window_size - 1 - first_part
        df.loc[:, 'score'] = np.concatenate((np.zeros(first_part), scores, np.zeros(second_part)))

        # normalize score
        df = normalize_column(df=df, column_name="score")

        # filter columns to be returned
        df = df.filter([value_column_name, "score", "normal_behavior"])

        scores = df["score"].tolist()
        normal_behavior = df["normal_behavior"].tolist()
        normalized_data = df[value_column_name].tolist()

        self.__result.set_computed_values(scores=scores,
                                          normal_behavior=normal_behavior,
                                          normalized_data=normalized_data)

    def get_result(self):
        return self.__result



