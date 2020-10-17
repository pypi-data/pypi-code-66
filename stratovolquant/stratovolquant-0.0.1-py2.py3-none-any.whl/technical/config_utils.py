import os
import configparser
from datetime import timedelta
from dateutil.relativedelta import *


class ConfigUtils:
    @staticmethod
    def read(filename):
        success, full_filename = ConfigUtils.find_full_filename(filename)
        if not success:
            raise Exception('Cannot find config filename {0}'.format(filename))

        interpolation = configparser.ExtendedInterpolation()
        config = configparser.ConfigParser(interpolation=interpolation, inline_comment_prefixes="#")
        config.read(full_filename)
        return config

    @staticmethod
    def parse_frequency(frequency_str):
        qty_str, unit_str = frequency_str.split()
        qty = int(qty_str)

        if unit_str == 'D':
            return timedelta(days=qty)
        elif unit_str == 'W':
            return timedelta(weeks=qty)
        elif unit_str == 'M':
            return relativedelta(months=qty)
        elif unit_str == 'Y':
            return relativedelta(years=qty)
        else:
            return None

    @staticmethod
    def find_full_filename(filename):
        success = False
        data_dir = None
        full_filename = None

        data_dir_list = ['../data/', '../../data/', '../../../data/']
        for data_dir in data_dir_list:
            if os.path.exists(data_dir):
                success = True
                break

        full_filename_list = [data_dir + 'private/' + filename,  data_dir + '/config/' + filename]
        if success:
            success = False
            for full_filename in full_filename_list:
                if os.path.isfile(full_filename):
                    success = True
                    break
        return success, full_filename
