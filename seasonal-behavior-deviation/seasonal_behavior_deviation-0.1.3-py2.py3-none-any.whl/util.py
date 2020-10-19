# -*- coding: utf-8 -*-
import logging
from skimage.util.shape import view_as_windows
import numpy as np
import pandas as pd

__author__ = "Jannik Frauendorf"
__copyright__ = "Jannik Frauendorf"
__license__ = "mit"

_logger = logging.getLogger(__name__)


def create_sliding_windows(series, window_size):
    """
    Computes the result of a sliding window over the given vector with the given window size.
    Each row represents the content of the sliding window at each position.

    :param series: pandas Series containing the time series
    :param window_size: an integer specifying the width of the sliding window.
    :return: pandas DataFrame
    """
    vector = np.array(series)
    return pd.DataFrame(view_as_windows(vector, window_size))


def normalize_column(df, column_name, new_column_name=None):
    """
    Normalize the given column in the given DatFrame linearly between 0 and 1.
    If no new_column_name is given the original data will be replaced.

    :param df: a pandas data frame that contains at least the given column_name
    :param column_name: a string that specifies the column name that should be normalized
    :param new_column_name: a string that specifies the column name of the normalized values
    :return: pandas DataFrame
    """

    if new_column_name is None:
        new_column_name = column_name

    column_min = df[column_name].min()
    column_max = df[column_name].max()

    # linear normalization
    df.loc[:, new_column_name] = (df[column_name] - column_min) / (column_max - column_min)
    return df


def adjust_normal_behavior_to_trend(normal_behavior: pd.Series, trend_diff: pd.Series) -> pd.Series:
    return normal_behavior - trend_diff


def detrend_series(series: pd.Series, season_length: int) -> (pd.Series, pd.Series):
    # extract overall trend via moving median
    trend = series.rolling(2 * season_length + 1, center=True).median()

    # the window computation creates NaNs at the beginning and at the end
    # these NaNs are filled with the median of this sequence
    first_window_remainder = series.iloc[[*range(season_length)]].index
    second_window_remainder = series.iloc[[*range(-season_length, 0)]].index
    trend.loc[first_window_remainder, ] = series.loc[first_window_remainder].median()
    trend.loc[second_window_remainder, ] = series.loc[second_window_remainder].median()

    overall_median = series.median()

    # compute the difference of the values to the trend (moving median) and adjust the values accordingly
    trend_diff = overall_median - trend
    detrended_values = series + trend_diff

    return trend_diff, detrended_values


def extract_normal_behavior(series: pd.Series, season_steps: pd.Series) -> pd.Series:
    """
    Extracts the normal behavior as the median of each season step.
    """

    df = pd.DataFrame({
        "season_step": season_steps,
        "value": series
    })

    # create normal behavior
    normal_behavior = df.groupby('season_step').agg({"value": "median"})["value"]

    # remove columns names and indices and create new clean series
    return pd.Series(data=normal_behavior.tolist())


def df_euclidean_distance(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.Series:
    """
    Computes the Euclidean Distance row-wise between two DataFrames.

    :param df1: pandas DataFrame containing numerical values
    :param df2: pandas DataFrame containing numerical values
    :return: pandas Series containing the Euclidean Distance
    """

    return pd.Series(np.linalg.norm(df1.values - df2.values, axis=1))

