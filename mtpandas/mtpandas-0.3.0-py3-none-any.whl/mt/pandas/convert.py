import pandas as _pd
from .csv import read_csv, to_csv


__all__ = ['dfload', 'dfsave']


def dfload(df_filepath, *args, **kwargs):
    '''Loads a dataframe file based on the file's extension.

    Parameters
    ----------
    df_filepath : str
        local path to an existing dataframe. The file extension is used to determine the file type.
    args : list
        list of positional arguments to pass to the corresponding reader
    kwargs : dict
        dictionary of keyword arguments to pass to the corresponding reader

    Returns
    -------
    pandas.DataFrame
        loaded dataframe

    Notes
    -----
    For '.csv' or '.csv.zip' files, we use :func:`mt.pandas.csv.read_csv`. For '.parquet' files, we use :func:`pandas.read_parquet`.

    Raises
    ------
    TypeError
        if file type is unknown
    '''

    path = df_filepath.lower()

    if path.endswith('.parquet'):
        return _pd.read_parquet(df_filepath, *args, **kwargs)

    if path.endswith('.csv') or path.endswith('.csv.zip'):
        return read_csv(df_filepath, *args, **kwargs)

    raise TypeError("Unknown file type: '{}'".format(df_filepath))


def dfsave(df, df_filepath, *args, **kwargs):
    '''Saves a dataframe to a file based on the file's extension.

    Parameters
    ----------
    df : pandas.DataFrame
        a dataframe
    df_filepath : str
        local path to an existing dataframe. The file extension is used to determine the file type.
    args : list
        list of positional arguments to pass to the corresponding writer
    kwargs : dict
        dictionary of keyword arguments to pass to the corresponding writer

    Returns
    -------
    object
        whatever the corresponding writer returns

    Notes
    -----
    For '.csv' or '.csv.zip' files, we use :func:`mt.pandas.csv.to_csv`. For '.parquet' files, we use :func:`pandas.DataFrame.to_parquet`.

    Raises
    ------
    TypeError
        if file type is unknown
    '''

    if not isinstance(df, _pd.DataFrame):
        raise TypeError("Input must be a pandas.DataFrame. Got '{}'.".format(type(df)))

    path = df_filepath.lower()

    if path.endswith('.parquet'):
        if not 'use_deprecated_int96_timestamps' in kwargs:
            kwargs = kwargs.copy()
            kwargs['use_deprecated_int96_timestamps'] = True # to avoid exception pyarrow.lib.ArrowInvalid: Casting from timestamp[ns] to timestamp[ms] would lose data: XXXXXXX
        return df.to_parquet(df_filepath, *args, **kwargs)

    if path.endswith('.csv') or path.endswith('.csv.zip'):
        return to_csv(df, df_filepath, *args, **kwargs)

    raise TypeError("Unknown file type: '{}'".format(df_filepath))


