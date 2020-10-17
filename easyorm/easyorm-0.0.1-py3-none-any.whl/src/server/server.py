import sys
import os
from .moduls import Modul
from .datasource import DataSource

class Server:

    @classmethod
    def run(cls):
        args = sys.argv
        if len(args) > 1 :
            params = args[1]
            if params == 'model':
                Modul.run()
            if params == 'run':
                os.system('python main.py')
            if params == 'datasource':
                DataSource.run()
