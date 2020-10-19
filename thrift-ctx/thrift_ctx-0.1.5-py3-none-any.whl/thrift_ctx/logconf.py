import datetime
import json
import logging
import os

from thrift_ctx import ctx

log_file = 'logs'
os.makedirs(log_file, exist_ok=True)

class RequestFormatter(logging.Formatter):

    def format(self, record: logging.LogRecord):
        try:
            if hasattr(record,"msg"):
                record.msg = record.msg.replace("\n", " *^* ")
        except:
            pass
        try:
            g = ctx.g
            record.req_id = g.request_id
        except (RuntimeError, AttributeError) as _:
            record.req_id = "******"


        return super(RequestFormatter, self).format(record)


class JSONFormatter(logging.Formatter):
    REMOVE_ATTR = [
        "args", "exc_info", "levelno", "pathname", "stack_info", "created", "msecs",
        "relativeCreated", "msg", "asctime",
    ]

    def format(self, record):
        try:
            if hasattr(record, "message"):
                record.message = record.message.replace("\n", " *^* ")
        except:
            pass
        try:
            g = ctx.g
            record.req_id = g.request_id
        except (RuntimeError, AttributeError) as _:
            record.req_id = "******"

        extra = self.build_record(record)
        self.set_format_time(extra)
        if record.exc_info:
            extra['exc_text'] = self.formatException(record.exc_info)

        return json.dumps(extra, ensure_ascii=False)

    @classmethod
    def build_record(cls, record):
        return {
            attr_name: record.__dict__[attr_name]
            for attr_name in record.__dict__
            if attr_name not in cls.REMOVE_ATTR
        }

    @classmethod
    def set_format_time(cls, extra):
        now = datetime.datetime.utcnow()
        format_time = now.strftime("%Y-%m-%dT%H:%M:%S" + ".%03d" % (now.microsecond / 1000) + "Z")
        extra['@timestamp'] = format_time
        return format_time


# log配置字典
conf = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'json': {
            'class': 'thrift_ctx.logconf.JSONFormatter',
        },
        'simple': {
            'format': '%(asctime)s|%(filename)12s:%(lineno)-4d|%(name)-10s|%(levelname)-7s|%(req_id)s|%(message)s',
            'datefmt': "%m-%d %H:%M:%S",
            'class': 'thrift_ctx.logconf.RequestFormatter',
        },
    },
    'filters': {},
    'handlers': {
        # 打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },

        # 全部打印到一个日志文件
        'details-bundle-file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'json',
            'filename': os.path.join(log_file, "bundle.log"),
            'maxBytes': 1024 * 1024 * 3,
            'backupCount': 40,
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'details-bundle-file'],
            'level': "DEBUG",
        },
        # system root logger
        'sys': {

        },

        # service root logger
        'svc': {

        },

        # util root logger
        'utl': {

        },

        # api root logger
        'api': {

        },

        # the logger of  default debug server
        'werkzeug': {
            'level': "ERROR"
        }
    },
}
