# -*- coding: utf-8 -*-
# Copyright (c) 2016 - 2020 Sqreen. All rights reserved.
# Please refer to our terms for more information:
#
#     https://www.sqreen.io/terms.html
#
""" Insert custom headers for Flask
"""
import logging

from .headers_insert import BaseHeadersInsertCB

LOGGER = logging.getLogger(__name__)


class HeadersInsertCBFlask(BaseHeadersInsertCB):
    """ Callback that add the custom sqreen header
    """

    def post(self, instance, args, kwargs, result=None, **options):
        """ Set headers
        """
        try:
            response = result
            for header_name, header_value in self.headers.items():
                response.headers.set(header_name, header_value)
        except Exception:
            LOGGER.warning("An error occurred", exc_info=True)

        return {}
