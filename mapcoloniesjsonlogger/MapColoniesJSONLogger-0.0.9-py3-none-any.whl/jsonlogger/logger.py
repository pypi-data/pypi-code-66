import logging, logging.config, time, yaml
from os import path
from pythonjsonlogger import jsonlogger

class JSONLogger(logging.Logger):
    """
    Logger with a json formatter
    """
    def __new__(cls, name, config_file=path.join(path.dirname(__file__), 'log.yaml'), additional_fields=None):
        """
        Constructor that creates a logger instance

        Args:
            name (str): name to associate with the logger
            config_file (str, optional): logging configuration yaml path. Defaults to path.join(path.dirname(__file__), 'log.yaml').
            additional_fields (dict, optional): dict of additional key/value pairs to log. Defaults to None.
        """
        # import logging configuration yaml
        with open(config_file, 'r') as log_config:
            # read the file to dict
            logging_config = yaml.safe_load(log_config)

            # configure logging using the logging configuration yaml
            logging.config.dictConfig(logging_config)

        # create logger and save it
        return CustomLoggerAdapter(logging.getLogger(name), additional_fields)


class CustomLoggerAdapter(logging.LoggerAdapter):
    def __init__(self, logger, additional_fields):
        super(CustomLoggerAdapter, self).__init__(logger, {})
        self.additional_fields = additional_fields

    def process(self, msg, kwargs):
        extra = self.extra.copy()
        extra.update(kwargs.get('extra', dict()))
        if self.additional_fields: extra.update(self.additional_fields)
        kwargs['extra'] = extra
        return msg, kwargs


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    """
    A custom json formatter
    """
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        if not log_record.get('timestamp'):
            # combine time with milliseconds to form a timestamp
            log_record['timestamp'] = time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime(record.created)) + f'.{round(record.msecs):03d}'
        if log_record.get('loglevel'):
            log_record['loglevel'] = log_record['loglevel'].upper()
        else:
            log_record['loglevel'] = record.levelname