from mock import MagicMock, patch
from nose.tools import eq_, raises

import gease.exceptions as exceptions
from gease.release import EndPoint


class TestPublish:
    def setUp(self):
        self.patcher = patch("gease.release.Api")
        self.fake_api_singleton = self.patcher.start()
        self.fake_api = MagicMock()
        self.fake_api_singleton.get_api = self.fake_api
        self.patcher2 = patch("gease.rest.get_token")
        self.fake_token = self.patcher2.start()
        self.fake_token.return_value = "token"

    def tearDown(self):
        self.patcher2.stop()
        self.patcher.stop()

    def test_create_release(self):
        self.fake_api.return_value = MagicMock(
            create=MagicMock(return_value={"html_url": "aurl"})
        )
        release = EndPoint("owner", "repo")
        release.publish(hello="world")

    @raises(exceptions.AbnormalGithubResponse)
    def test_unknown_error(self):
        self.fake_api.return_value = MagicMock(
            create=MagicMock(return_value={})
        )
        release = EndPoint("owner", "repo")
        release.publish(hello="world")

    @raises(exceptions.AbnormalGithubResponse)
    def test_release_exist(self):
        self.fake_api.return_value = MagicMock(
            create=MagicMock(side_effect=exceptions.ReleaseExistException)
        )
        release = EndPoint("owner", "repo")
        release.publish(hello="world", tag_name="existing tag")

    @raises(exceptions.AbnormalGithubResponse)
    def test_repo_not_found(self):
        self.fake_api.return_value = MagicMock(
            create=MagicMock(side_effect=exceptions.RepoNotFoundError)
        )
        release = EndPoint("owner", "repo")
        release.republish = MagicMock(side_effect=exceptions.RepoNotFoundError)
        release.publish(hello="world")

    @raises(exceptions.AbnormalGithubResponse)
    def test_unhandled_exception(self):
        self.fake_api.return_value = MagicMock(
            create=MagicMock(side_effect=exceptions.UnhandledException)
        )
        release = EndPoint("owner", "repo")
        release.publish(hello="world")


class TestRepublish:
    def setUp(self):
        self.patcher = patch("gease.release.Orgs")
        self.fake_orgs = self.patcher.start()
        self.patcher2 = patch("gease.release.Repo")
        self.fake_repo = self.patcher2.start()
        self.patcher3 = patch("gease.release.Api")
        self.fake_api_singleton = self.patcher3.start()
        self.fake_api = MagicMock()
        self.fake_api_singleton.get_api = self.fake_api

    def tearDown(self):
        self.patcher3.stop()
        self.patcher2.stop()
        self.patcher.stop()

    def test_create_release(self):
        test_url = "special url"
        self.fake_orgs.return_value = MagicMock(
            get_all_organisations=MagicMock(
                return_value=[{"repos_url": "repo", "login": "zhangfei"}]
            )
        )
        self.fake_repo.return_value = MagicMock(
            get_all_repos=MagicMock(return_value=[{"name": "repo"}])
        )
        self.fake_api.return_value = MagicMock(
            create=MagicMock(return_value={"html_url": test_url})
        )
        release = EndPoint("owner", "repo")
        ret = release.republish(hello="world")
        eq_(ret, test_url)
