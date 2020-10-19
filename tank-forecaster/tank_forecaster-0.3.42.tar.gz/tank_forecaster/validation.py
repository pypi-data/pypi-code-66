# libraries
from datetime import datetime, timedelta

import numpy as np
import pandas as pd


def format_tank(dict_input, freq: str = "30min"):

    if dict_input is None:
        return None

    validated_input = []

    for i in range(len(dict_input)):
        if "read_time" in dict_input[i] and "volume" in dict_input[i]:
            validated_input.append(dict_input[i])

    if validated_input == []:
        return None

    validated_input = sorted(validated_input, key=lambda x: x["read_time"])
    validated_input = [d for d in validated_input if d["volume"]]
    df = pd.DataFrame(validated_input)
    df.read_time = pd.to_datetime(df.read_time)
    df["y"] = df.volume.diff() * -1
    df = df[["read_time", "y"]].rename(columns={"read_time": "ds"})
    df = df[df.y < 800].copy()
    df.y = df.y.clip(lower=0)
    df = df.set_index("ds").groupby(pd.Grouper(freq=freq)).sum()

    if len(df) == 2:
        return None

    df.reset_index(level=0, inplace=True)
    output = df.iloc[1:-1]

    return output


def format_sales(dict_input):

    if dict_input == [] or dict_input is None:
        return None

    dict_input = sorted(dict_input, key=lambda x: x["date"])
    dat = pd.DataFrame(dict_input)
    df = dat[["date", "sales"]]

    df2 = df.copy()
    df2["sales"] = df["sales"].clip(
        lower=df.sales.quantile(0.015), upper=df.sales.quantile(0.995)
    )

    df3 = df2.rename(columns={"date": "ds", "sales": "y"})

    df4 = df3.copy()
    df4["ds"] = df3.loc[:, "ds"].astype("datetime64[ns]")

    return df4


def gen_past(df, freq="30min", periods=432):

    if len(df) == 0 or df is None:
        now = datetime.now()
        end_0 = now - (now - datetime.min) % timedelta(minutes=30)

    else:
        end_0 = df.iloc[-1, 0]

    past = pd.date_range(end=end_0, freq=freq, periods=periods)
    past = pd.DataFrame(past)
    past.rename(columns={0: "ds"}, inplace=True)
    past["ds"] = pd.to_datetime(past["ds"], format="%Y-%m-%d")

    return past


def validate_tank(tank_data, sales_data):

    if len(tank_data) == 0 or tank_data is None:
        return None

    # add day of year for tank data / sales data
    sales_data["doy"] = sales_data["ds"].dt.dayofyear
    sales_data = sales_data.iloc[-100:]

    # create validation dataframe
    val_matrix = np.zeros((432, 2))
    val_df = pd.DataFrame(val_matrix, columns=["ds", "doy"])

    # dynamically generate timestamps
    val_df["ds"] = gen_past(tank_data, freq="30min", periods=432)
    val_df["doy"] = val_df.ds.dt.dayofyear
    val_df["ts"] = val_df.ds.dt.time

    val_df = pd.merge(
        left=val_df, right=generic_daily_decomp, how="left", left_on="ts", right_on="ts"
    )
    val_df = pd.merge(
        left=val_df, right=tank_data, how="left", left_on="ds", right_on="ds"
    )
    val_df = pd.merge(
        left=val_df, right=sales_data, how="left", left_on="doy", right_on="doy"
    )

    val_df.rename(columns={"ds_x": "ds", "y_x": "actual", "y_y": "daily"}, inplace=True)
    val_df = val_df.loc[:, ["ds", "ts", "actual", "daily", "daily_multi"]]

    # calculate generalized daily tank sticking curve from sales data
    val_df["base_est"] = val_df.loc[:, "daily"] * (1 / 48)
    est = val_df["base_est"] * val_df["daily_multi"]
    val_df["estimated"] = est

    val_df = val_df.loc[:, ["ds", "actual", "estimated"]]

    # data abnormalities adjustment
    diff = val_df.estimated - val_df.actual
    threshold = diff.abs().quantile(0.95)

    mask_adj = diff.abs() > threshold
    mask_tank = [not i for i in mask_adj]

    # val_df.loc[mask_adj, 'output'] = val_df.loc[mask_adj, 'adj_sales']
    # val_df.loc[mask_tank, 'output'] = val_df.loc[mask_tank, 'tank_vals']

    # missing data imputation
    mask_nan = val_df.actual.isna()
    mask_not_nan = [not i for i in mask_nan]

    val_df.loc[mask_nan, "y"] = val_df.loc[mask_nan, "estimated"]
    val_df.loc[mask_not_nan, "y"] = val_df.loc[mask_not_nan, "actual"]

    # for testing purposes, uncomment this
    # return val_df

    # for use in forecasting, uncomment this
    val_df.rename(columns={"ds_x": "ds"}, inplace=True)

    return val_df[["ds", "y"]]


if __name__ == "__main__":
    raw_readings = [
        {
            "id": "5f8de916228d65344402f0a7",
            "store_number": "110",
            "tank_id": "1",
            # "run_time": "2020-10-19T19:29:17",
            # "read_time": "2020-10-19T19:29:23",
            "volume": 13547.508587862303,
            "temperature": 48.1715720177702,
        },
        {
            "id": "5f8de914228d65344402f083",
            "store_number": "110",
            "tank_id": "1",
            "run_time": "2 020-10-19T19:29:16",
            # "read_time": "2020-10-19T19:29:21",
            # "volume": 13549.028743568035,
            "temperature": 48.1710855651926,
        },
        {
            "id": "5f8de49c1c6cbdc17a3546f9",
            "store_number": "110",
            "tank_id": "1",
            # "run_time": "2020-10-19T19:10:13",
            # "read_time": "2020-10-19T19:10:18",
            "volume": 13621.377813533778,
            "temperature": 48.0932317562486,
        },
        {
            "id": "5f8de49b1c6cbdc17a3546e5",
            "store_number": "110",
            "tank_id": "1",
            "run_time": "2020-10-19T19:10:13",
            "read_time": "2020-10-19T19:10:16",
            # "volume": 13621.377813533778,
            "temperature": 48.0932317562486,
        },
        {
            "id": "5f8de0011dff1f3a8c927fc1",
            "store_number": "110",
            "tank_id": "1",
            "run_time": "2020-10-19T18:50:35",
            "read_time": "2020-10-19T18:50:37",
            # "volume": 13792.582207190737,
            "temperature": 48.025463112635,
        },
    ]
    format_tank(raw_readings)
