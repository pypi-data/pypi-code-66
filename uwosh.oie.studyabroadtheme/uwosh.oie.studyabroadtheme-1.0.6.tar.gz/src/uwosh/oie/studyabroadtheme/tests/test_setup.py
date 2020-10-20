# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone.browserlayer import utils
from Products.CMFPlone.utils import get_installer
from uwosh.oie.studyabroadtheme.testing import UWOSH_OIE_STUDYABROADTHEME_INTEGRATION_TESTING as testing_layer  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that uwosh.oie.studyabroadtheme is properly installed."""

    layer = testing_layer

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = get_installer(self.portal)

    def test_product_installed(self):
        """Test if uwosh.oie.studyabroadtheme is installed."""
        self.assertTrue(self.installer.is_product_installed(
            'uwosh.oie.studyabroadtheme'))

    def test_browserlayer(self):
        """Test that IUwoshOieStudyabroadthemeLayer is registered."""
        from uwosh.oie.studyabroadtheme.interfaces import (  # isort:skip
            IUwoshOieStudyabroadthemeLayer)
        self.assertIn(
            IUwoshOieStudyabroadthemeLayer,
            utils.registered_layers(),
        )


class TestUninstall(unittest.TestCase):

    layer = testing_layer

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = get_installer(self.portal)
        self.installer.uninstallProducts(['uwosh.oie.studyabroadtheme'])

    def test_product_uninstalled(self):
        """Test if uwosh.oie.studyabroadtheme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'uwosh.oie.studyabroadtheme'))

    def test_browserlayer_removed(self):
        """Test that IUwoshOieStudyabroadthemeLayer is removed."""
        from uwosh.oie.studyabroadtheme.interfaces import (  # isort:skip
            IUwoshOieStudyabroadthemeLayer)
        self.assertNotIn(
            IUwoshOieStudyabroadthemeLayer,
            utils.registered_layers(),
        )
