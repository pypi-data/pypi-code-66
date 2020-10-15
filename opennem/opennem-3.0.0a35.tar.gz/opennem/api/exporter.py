import logging
import os
from datetime import datetime

from smart_open import open

from opennem.api.stats.router import (
    energy_network_fueltech_api,
    power_network_fueltech_api,
    price_network_region_api,
)
from opennem.api.weather.router import station_observations_api
from opennem.db import get_database_engine

YEAR_MIN = 2010

BASE_EXPORT = "s3://data.opennem.org.au"

BASE_EXPORT_LOCAL = os.path.realpath(
    os.path.join(os.path.dirname(__file__), "..", "..", "data")
)


UPLOAD_ARGS = {
    "ContentType": "application/json",
}

logger = logging.getLogger(__name__)


def wem_export_power():
    engine = get_database_engine()

    stat_set = power_network_fueltech_api(
        network_code="WEM",
        network_region="WEM",
        interval="30m",
        period="7d",
        engine=engine,
    )

    weather = station_observations_api(
        station_code="009021",
        interval="10m",
        period="7d",
        network_code="WEM",
        engine=engine,
    )

    price = price_network_region_api(
        engine=engine,
        network_code="WEM",
        region_code="WEM",
        interval="30m",
        period="7d",
    )

    # demand = wem_demand()

    stat_set.data = stat_set.data + price.data
    stat_set.data = stat_set.data + weather.data

    power_path = BASE_EXPORT + "/power/wem.json"

    with open(
        power_path,
        "w",
        transport_params=dict(multipart_upload_kwargs=UPLOAD_ARGS),
    ) as fh:
        fh.write(stat_set.json())


def wem_export_years():
    engine = get_database_engine()

    for year in range(datetime.now().year, YEAR_MIN - 1, -1):

        stat_set = None

        try:
            stat_set = energy_network_fueltech_api(
                network_code="WEM",
                network_region="WEM",
                interval="1d",
                year=year,
                period="1Y",
                engine=engine,
            )
        except Exception as e:
            logger.error(
                "Could not get energy network fueltech for {} {} : {}".format(
                    "WEM", year, e
                )
            )
            continue

        # market_value = wem_market_value_year(year)

        year_path = BASE_EXPORT + f"/wem/energy/daily/{year}.json"

        with open(
            year_path,
            "w",
            transport_params=dict(multipart_upload_kwargs=UPLOAD_ARGS),
        ) as fh:
            fh.write(stat_set.json())


def wem_export_all():

    engine = get_database_engine()

    stat_set = energy_network_fueltech_api(
        network_code="WEM",
        network_region="WEM",
        interval="1M",
        period="10Y",
        engine=engine,
    )

    # market_value = wem_market_value_all()

    all_path = BASE_EXPORT + "/wem/energy/monthly/all.json"

    with open(
        all_path,
        "w",
        transport_params=dict(multipart_upload_kwargs=UPLOAD_ARGS),
    ) as fh:
        fh.write(stat_set.json())


def wem_run_all():
    wem_export_power()
    wem_export_years()
    wem_export_all()


if __name__ == "__main__":
    wem_run_all()
