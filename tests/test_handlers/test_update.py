from fastapi.testclient import TestClient

from restfull.domain import const
from restfull.domain.entities.user import BaseUser
from restfull.infrastructure.api.endpoints.update_user import ErrorWithUpdateResponse
from restfull.infrastructure.auth.schemas import UserCreate


def test_update_user(client: TestClient, default_user_create: UserCreate, authorize_cookie):
    update_user = BaseUser(id=1, **default_user_create.model_dump())
    update_user.name = "new_name"
    response = client.put(const.API_PREFIX, cookies=authorize_cookie, json=update_user.to_dict())
    assert response.status_code == 200
    assert response.json()["payload"]["id"] == update_user.id
    assert response.json()["payload"]["name"] == update_user.name


def test_fail_update_user(client: TestClient, authorize_cookie):
    response = client.put(const.API_PREFIX, json={"error": True}, cookies=authorize_cookie)
    assert response.status_code == 422
    assert "detail" in response.json().keys()


def test_unauthorized_user(client: TestClient):
    response = client.put(const.API_PREFIX, json={"id": 5, "name": "Carl"})
    assert response.status_code == 401
    assert "detail" in response.json().keys()


def test_fail_update_user_not_exist(client: TestClient, authorize_cookie):
    response = client.put(const.API_PREFIX, json={"id": 5, "name": "Carl"}, cookies=authorize_cookie)
    assert response.status_code == 500
    assert response.json() == ErrorWithUpdateResponse().model_dump()
    assert response.json()["result"] == "error"
    assert response.json()["payload"] == "See logs"
