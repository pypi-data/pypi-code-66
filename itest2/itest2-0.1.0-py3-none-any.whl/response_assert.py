# -*- coding: utf-8 -*-

from requests.models import Response
from hamcrest.core.base_matcher import BaseMatcher


class StatusCodeChecker(BaseMatcher):

    def __init__(self, expected):
        self.expected = expected

    def _matches(self, actual):
        if isinstance(actual, Response):
            if actual.status_code == self.expected:
                return True
            else:
                return False
        else:
            raise TypeError("expected a requests' Response")

    def describe_to(self, description):
        description.append_text(f'{self.expected}\n')
