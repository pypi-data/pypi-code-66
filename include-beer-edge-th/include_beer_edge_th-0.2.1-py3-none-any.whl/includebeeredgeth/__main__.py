# main script for Temperature Humidity package
__version__ = "0.2.1"

import os
import importlib
import core.config.manager as cfg_mgr
import core.utils.logging as logger
import core.utils.csv as csv

# Set config object
config = cfg_mgr.ConfigManager()

# Set stats objects
stats_buffer = {}
stats_field_names = ['timestamp', 'temperature', 'humidity']
stats_file = __package__ + '.csv'
stats_dir = os.path.expanduser(config.stats_dir)
if not os.path.exists(stats_dir):
    os.makedirs(stats_dir)

# Set logging objects
log_buffer = []
log_dir = os.path.expanduser(config.log_dir)
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
log_file = os.path.join(log_dir, __package__ + '.log')
log_this = logger.load_logger(
    __package__, log_file, config.debugging)

# Load ambient sensor module
ambient_sensor = config.ambient_sensor.type
log_this.debug('Set ambient sensor to: ' + ambient_sensor)
try:
    a_sensor = importlib.import_module(ambient_sensor)
except Exception as e:
    log_this.error('Error loading ambient sensor: ' +
                    ambient_sensor + ' exception: ' + str(e))

# Get ambient temperature and humidity
ambient_temp, ambient_humidity = a_sensor.read(config.ambient_sensor.pin)
if isinstance(ambient_temp, (float, int)) and isinstance(ambient_humidity, (float, int)):
    stats_buffer['ambient_humidity'] = ambient_humidity
    stats_buffer['ambient_temperature'] = ambient_temp
    csv.dict_writer(stats_file, stats_field_names, stats_buffer)
    log_buffer.append('A/T: ' + str(ambient_temp))
    log_buffer.append('A/H: ' + str(ambient_humidity))
    log_this.info(' | '.join(map(str, log_buffer)))
else:
    log_this.error('Error reading ' + config.ambient_sensor.type + 
        ' : ' + str(ambient_temp) + ' ' + str(ambient_humidity))
