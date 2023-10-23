from fastapi.testclient import TestClient

from restfull.domain import const
from restfull.infrastructure.api.application import application

client = TestClient(application)


def test_get_users():
    response = client.get(const.API_PREFIX)
    assert response.status_code == 200
    assert len(response.json()) > 0