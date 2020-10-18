import os

from mock import patch
from nose.tools import eq_, raises

import gease.constants as constants
import gease.exceptions as exceptions
from gease.utils import get_info


class TestMain:
    def setUp(self):
        self.patcher = patch("gease.utils.os.path.expanduser")
        self.fake_expand = self.patcher.start()
        self.fake_expand.return_value = os.path.join("tests", "fixtures")

    def tearDown(self):
        self.patcher.stop()

    def test_get_token(self):
        self.fake_expand.return_value = os.path.join("tests", "fixtures")
        user = get_info(constants.KEY_GEASE_TOKEN)
        eq_(user, "test")

    @raises(exceptions.NoGeaseConfigFound)
    def test_no_gease_file(self):
        self.fake_expand.return_value = os.path.join("tests")
        get_info(constants.KEY_GEASE_TOKEN)

    @raises(KeyError)
    def test_wrong_key(self):
        self.fake_expand.return_value = os.path.join(
            "tests", "fixtures", "malformed"
        )
        get_info(constants.KEY_GEASE_TOKEN)
