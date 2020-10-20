import structlog
import logging
import sys
import os

from structlog import wrap_logger
from structlog.processors import JSONRenderer
from structlog.stdlib import filter_by_level
from structlog.stdlib import add_log_level_number

import ddtrace
from ddtrace.helpers import get_correlation_ids


def tracer_injection(logger, log_method, event_dict):
    # get correlation ids from current tracer context
    trace_id, span_id = get_correlation_ids()

    # add ids to structlog event dictionary
    event_dict["dd.trace_id"] = trace_id or 0
    event_dict["dd.span_id"] = span_id or 0

    # add the env, service, and version configured for the tracer
    event_dict["dd.env"] = ddtrace.config.env or ""
    event_dict["dd.service"] = ddtrace.config.service or ""
    event_dict["dd.version"] = ddtrace.config.version or ""

    return event_dict


def rename_message_key(_, __, event_dict):
    event_dict["message"] = event_dict["event"]
    event_dict.pop("event", None)
    return event_dict


def increase_level_numbers(_, __, event_dict):
    event_dict["level"] = event_dict["level_number"] * 10
    event_dict.pop("level_number", None)
    return event_dict


level = os.getenv("LOG_LEVEL", "INFO")

logging.basicConfig(stream=sys.stdout, format="%(message)s", level=level)
bufflog = wrap_logger(
    logging.getLogger(__name__),
    processors=[
        tracer_injection,
        filter_by_level,
        rename_message_key,
        add_log_level_number,
        increase_level_numbers,
        JSONRenderer(),
    ],
)
