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

from . import freeze
from . import flask
from . import logger
from . import pages


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

        """Setup Markdown page processing.
        """
        pages.init_app(self.app)

        """Create static pages from generated pages.
        """
        freeze.init_app(self.app)

        self.generate_pages(app)

        if 'build' in environment:
            freeze.freeze()

        logger.info('rStatic exited with 0.')

    def generate_pages(self, app):
        """Generate site pages.

        Create an index and other pages from the `pages` directory.

        :param (class) self
            The representation of the instantiated Class Instance
        :param (str) app
            The application object to attach the routes to
        """
        logger.info('rStatic is generating static index and user-named pages')

        @app.route('/', methods=['GET'])
        def core_index_get():
            """Index page.

            :return (object) render_template
                A dynamically rendered HTML page.
            """
            page = pages.get_or_404('index')

            template = page.meta.get('template', 'page.html')

            return render_template(template, page=page)

        @app.route('/<path:path>/', methods=['GET'])
        def core_page_get(path):
            """Dynamically routed (you-name-it) pages.

            :return (object) render_template
                A dynamically rendered HTML page.
            """
            page = pages.get_or_404(path)

            template = page.meta.get('template', 'page.html')

            return render_template(template, page=page)

        @freeze.register_generator
        def core_page_get():
            """URL Generator.

            Freeze pages from these routes when building static pages to the
            static `build` directory.

            See official Frozen Flask documentation for more information.
            http://pythonhosted.org/Frozen-Flask/#url-generators
            """
            for page in pages:
                logger.info('rStatic is creating static page for %s',
                            page['path'])
                yield {'path': page['path']}
