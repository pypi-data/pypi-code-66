import pytest
from insnail_ai_tools.web import create_fast_api_app
from fastapi.testclient import TestClient

app = create_fast_api_app(cors=True, health_check=True)
client = TestClient(app)


def test_fast_api_health_check():
    response = client.get("/health-check")
    assert response.status_code == 200
