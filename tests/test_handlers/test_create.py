from fastapi.testclient import TestClient

from restfull.domain import const
from restfull.domain.entities.user import UserWhitPassword


def test_create_user(client: TestClient, delete_default_user):
    test_user = UserWhitPassword()
    response = client.post(const.API_PREFIX, json=test_user.to_dict())
    assert response.status_code == 200
    assert response.json() is True