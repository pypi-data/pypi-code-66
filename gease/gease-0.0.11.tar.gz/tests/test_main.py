import os
import sys

import mock
from nose.tools import raises

import gease.exceptions as exceptions
from gease.main import main, fatal
from gease.constants import DEFAULT_RELEASE_MESSAGE

TEST_TAG = "tag"
SHORT_ARGS = ["gs", "repo", TEST_TAG]


class TestMain:
    def setUp(self):
        self.patcher = mock.patch("gease.utils.os.path.expanduser")
        self.fake_expand = self.patcher.start()
        self.fake_expand.return_value = os.path.join("tests", "fixtures")

        self.patcher2 = mock.patch("gease.main.EndPoint")
        self.fake_release = self.patcher2.start()

    def tearDown(self):
        self.patcher2.stop()
        self.patcher.stop()

    @raises(SystemExit)
    def test_key_error_in_main(self):
        self.fake_expand.return_value = os.path.join(
            "tests", "fixtures", "malformed"
        )
        with mock.patch.object(sys, "argv", SHORT_ARGS):
            main()

    @raises(SystemExit)
    def test_no_gease_file_in_main(self):
        self.fake_expand.return_value = os.path.join("tests")
        with mock.patch.object(sys, "argv", SHORT_ARGS):
            main()

    def test_good_commands(self):
        create_method = mock.MagicMock(
            return_value="http://localhost/tag/testurl"
        )
        self.fake_release.return_value = mock.MagicMock(publish=create_method)
        with mock.patch.object(sys, "argv", SHORT_ARGS):
            main()
            create_method.assert_called_with(
                tag_name=TEST_TAG, name=TEST_TAG, body=DEFAULT_RELEASE_MESSAGE
            )

    def test_custom_release_message(self):
        release_message = ["hello", "world", "you", "see", "it"]
        create_method = mock.MagicMock(
            return_value="http://localhost/tag/testurl"
        )
        self.fake_release.return_value = mock.MagicMock(publish=create_method)
        with mock.patch.object(sys, "argv", SHORT_ARGS + release_message):
            main()
            create_method.assert_called_with(
                tag_name=TEST_TAG,
                name=TEST_TAG,
                body=" ".join(release_message),
            )

    def test_quoted_release_message(self):
        release_message = "hello world you see it"
        create_method = mock.MagicMock(
            return_value="http://localhost/tag/testurl"
        )
        self.fake_release.return_value = mock.MagicMock(publish=create_method)
        with mock.patch.object(sys, "argv", SHORT_ARGS + [release_message]):
            main()
            create_method.assert_called_with(
                tag_name=TEST_TAG, name=TEST_TAG, body=release_message
            )

    @raises(SystemExit)
    def test_error_response(self):
        create_method = mock.MagicMock(
            side_effect=exceptions.AbnormalGithubResponse
        )
        self.fake_release.return_value = mock.MagicMock(publish=create_method)
        with mock.patch.object(sys, "argv", SHORT_ARGS):
            main()
            create_method.assert_called_with(
                tag_name=TEST_TAG, name=TEST_TAG, body=DEFAULT_RELEASE_MESSAGE
            )


@raises(SystemExit)
def test_no_args():
    with mock.patch.object(sys, "argv", []):
        main()


@raises(SystemExit)
def test_insufficent_args():
    with mock.patch.object(sys, "argv", SHORT_ARGS[:2]):
        main()


@raises(SystemExit)
def test_fatal_message():
    fatal("message and we quit")
