from mock import MagicMock, patch
from nose.tools import eq_

from gease.orgs import EndPoint as Org
from gease.repo import EndPoint as Repo


class TestOrgEndPoint:
    def setUp(self):
        self.patcher = patch("gease.orgs.Api")
        self.fake_api_singleton = self.patcher.start()
        self.get = MagicMock()
        self.fake_api_singleton.get_api = MagicMock(
            return_value=MagicMock(get=self.get)
        )

    def tearDown(self):
        self.patcher.stop()

    def test_orgs(self):
        test_return = "hei"
        self.get.return_value = test_return

        org = Org()
        response = org.get_all_organisations()
        eq_(test_return, response)


class TestRepoEndPoint:
    def setUp(self):
        self.patcher = patch("gease.repo.Api")
        self.fake_api_singleton = self.patcher.start()
        self.get = MagicMock()
        self.fake_api_singleton.get_api = MagicMock(
            return_value=MagicMock(get=self.get)
        )

    def tearDown(self):
        self.patcher.stop()

    def test_repo(self):
        test_return = "hei"
        self.get.return_value = test_return

        repo = Repo()
        response = repo.get_all_repos()
        eq_(test_return, response)
