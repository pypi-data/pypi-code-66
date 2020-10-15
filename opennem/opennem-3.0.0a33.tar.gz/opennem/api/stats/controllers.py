from collections import OrderedDict
from datetime import datetime, timezone
from itertools import groupby
from operator import attrgetter
from typing import List, Optional, Union

from pytz import timezone as pytz_timezone
from sqlalchemy.orm import Session

from opennem.db.models.opennem import FacilityScada, Station
from opennem.schema.network import NetworkSchema
from opennem.schema.time import TimeInterval, TimePeriod
from opennem.schema.units import UnitDefinition
from opennem.utils.time import human_to_timedelta
from opennem.utils.timezone import make_aware

from .schema import (
    DataQueryResult,
    OpennemData,
    OpennemDataHistory,
    OpennemDataSet,
)


def stats_factory(
    stats: List[DataQueryResult],
    interval: TimeInterval,
    period: TimePeriod,
    units: UnitDefinition,
    network: Optional[NetworkSchema] = None,
    timezone: Optional[Union[timezone, pytz_timezone]] = None,
    code: Optional[str] = None,
    region: Optional[str] = None,
    fueltech_group: bool = False,
    group_field: str = None,
) -> Optional[OpennemDataSet]:
    """
        Takes a list of data query results and returns OpennemDataSets

        @TODO optional groupby field
        @TODO override timezone
    """

    if network:
        timezone = network.get_timezone()

    dates = [s.interval for s in stats]

    start = min(dates)
    end = max(dates)

    if timezone:
        start = make_aware(min(dates), timezone)
        end = make_aware(max(dates), timezone)

    # free
    dates = []

    group_codes = list(set([i.group_by for i in stats if i.group_by]))

    stats_grouped = []

    for group_code in group_codes:

        data_grouped = dict()

        for stat in stats:
            if stat.interval not in data_grouped:
                data_grouped[stat.interval] = None

            if stat.group_by == group_code:
                data_grouped[stat.interval] = stat.result

        data_sorted = OrderedDict(sorted(data_grouped.items()))

        history = OpennemDataHistory(
            start=start,
            last=end,
            interval=interval.interval_human,
            data=list(data_sorted.values()),
        )

        data = OpennemData(
            data_type=units.unit_type,
            units=units.unit,
            code=group_code,
            interval=interval,
            period=period,
            history=history,
        )

        if network:
            data.network = network.code

        # *sigh* - not the most flexible model
        if fueltech_group:
            data.fuel_tech = group_code
            data.id = ".".join(
                [network.code, "fueltech", group_code, units.unit_type]
            )
            # @TODO make this an alias
            data.type = units.unit_type

        if group_field:
            group_fields = []

            # setattr(data, group_field, group_code)

            if network:
                group_fields.append(network.code)

            group_fields + [group_field, group_code, units.unit_type]

            data.id = ".".join(group_fields)
            data.type = units.unit_type

        if region:
            data.region = region

        stats_grouped.append(data)

    stat_set = OpennemDataSet(
        data_type=units.unit_type,
        data=stats_grouped,
        created_at=datetime.now(),
        code=code,
    )

    if network:
        stat_set.network = network.code

    if region:
        stat_set.region = region

    return stat_set


def station_attach_stats(station: Station, session: Session) -> Station:
    # @TODO update for new queries
    since = datetime.now() - human_to_timedelta("7d")

    facility_codes = list(set([f.code for f in station.facilities]))

    stats = (
        session.query(FacilityScada)
        .filter(FacilityScada.facility_code.in_(facility_codes))
        .filter(FacilityScada.trading_interval >= since)
        .order_by(FacilityScada.facility_code)
        .order_by(FacilityScada.trading_interval)
        .all()
    )

    for facility in station.facilities:
        facility_power = list(
            filter(lambda s: s.facility_code == facility.code, stats)
        )

        # facility.scada_power = stats_factory(facility_power)

    return station
