from fastapi.testclient import TestClient

from restfull.domain import const
from restfull.domain.entities.user import BaseUserWhitPassword


def test_update_user(client: TestClient, create_user_and_teardown):
    test_user = BaseUserWhitPassword(id=1, name="new_name")
    response = client.put(const.API_PREFIX, json=test_user.to_dict())
    assert response.status_code == 200
    assert response.json()["id"] == test_user.id
    assert response.json()["name"] == test_user.name
