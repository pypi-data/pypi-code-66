#!/usr/bin/env python

"""rStatic (Rebatch Static Site Generator).

Create by Joshua Powell on 2020-OCT-16.

Copyright (c) 2020 Joshua Powell. All rights reserved.

For license and copyright information please see the LICENSE.md (the "License")
document packaged with this software. This file and all other files included in
this packaged software may not be used in any manner except in compliance with
the License. Software distributed under this License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTY, OR CONDITIONS OF ANY KIND, either express or
implied.

See the License for the specific language governing permission and limitations
under the License.
"""


import os

from . import flask
from . import logger


class Application(object):
    """Create class-based Flask application."""

    def __init__(self, name, environment="default", ):
        """Application Constructor.

        :param (class) self
            The representation of the instantiated Class Instance
        :param (str) name
            The name of the application
        :param (str) environment
            The name of the enviornment in which to load the application
        """
        self.name = name
        self.environment = environment

        """Create our base Flask application
        """
        logger.info('Starting rStatic')
        app = flask.Flask(__name__, static_url_path='/static')

        self.app = app

        """Import configuration based on environment.
        """
        logger.info('Locating environment configuration file')

        config_ = ('%s/config/%s.json') % (os.getcwd(), environment)

        """Parse the JSON configuration file content.
        """
        logger.info('Loading environment variables from configuration file')
        self.app.config.from_json(config_)

        logger.info('rStatic exited with 0.')
