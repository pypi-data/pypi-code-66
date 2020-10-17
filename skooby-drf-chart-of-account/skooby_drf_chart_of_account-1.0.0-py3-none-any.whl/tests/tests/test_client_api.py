"""Test cases for LayerModel views apis."""
from django.test import TestCase
from rest_framework.test import RequestsClient


class LayerViewsAPITestCases(TestCase):
    """Testing various apis of the Layer views."""

    client = RequestsClient()

    def test_get_request_apis(self):
        """Test all layers viewsets apis."""
        request = self.client.get('http://127.0.0.1:8000/accounts/charts/layer/one/')
        self.assertEqual(request.status_code, 200)
        request = self.client.get('http://127.0.0.1:8000/accounts/charts/layer/two/')
        self.assertEqual(request.status_code, 200)
        request = self.client.get('http://127.0.0.1:8000/accounts/charts/layer/three/')
        self.assertEqual(request.status_code, 200)
        request = self.client.get('http://127.0.0.1:8000/accounts/charts/layer/four/')
        self.assertEqual(request.status_code, 200)
        request = self.client.get('http://127.0.0.1:8000/accounts/charts/layer/five/')
        self.assertEqual(request.status_code, 200)
        request = self.client.get('http://127.0.0.1:8000/accounts/charts/layer/one/1/')
        self.assertEqual(request.status_code, 404)
