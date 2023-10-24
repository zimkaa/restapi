from fastapi.testclient import TestClient

from restfull.domain import const
from restfull.domain.entities.user import BaseUserWhitPassword
from restfull.infrastructure.api.endpoints.update_user import ErrorWithUpdateResponse


def test_update_user(client: TestClient, create_user_and_teardown):
    update_user = BaseUserWhitPassword(id=1, name="new_name")
    response = client.put(const.API_PREFIX, json=update_user.to_dict())
    assert response.status_code == 200
    assert response.json()["payload"]["id"] == update_user.id
    assert response.json()["payload"]["name"] == update_user.name


def test_fail_update_user(client: TestClient, create_user_and_teardown):
    response = client.put(const.API_PREFIX, json={"error": True})
    assert response.status_code == 422
    assert "detail" in response.json().keys()


def test_fail_update_user_not_exist(client: TestClient):
    response = client.put(const.API_PREFIX, json={"id": 5, "name": "Carl"})
    assert response.status_code == 500
    assert response.json() == ErrorWithUpdateResponse().model_dump()
    assert response.json()["result"] == "error"
    assert response.json()["payload"] == "See logs"
