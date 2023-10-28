from fastapi.testclient import TestClient

from restfull.domain import const
from restfull.infrastructure.api.endpoints.delete_user import ErrorNoUserResponse
from restfull.infrastructure.api.responses.base import OkResponse


def test_delete_user(client: TestClient, authorize_cookie):
    user_id = 1
    response = client.delete(f"{const.API_PREFIX}/{user_id}", cookies=authorize_cookie)
    assert response.status_code == 200
    assert response.json() == OkResponse().model_dump()


def test_fail_delete_user(client: TestClient, authorize_cookie):
    user_id = 100
    response = client.delete(f"{const.API_PREFIX}/{user_id}", cookies=authorize_cookie)
    assert response.status_code == 404
    assert response.json() == ErrorNoUserResponse().model_dump()
    assert response.json()["result"] == "error"
    assert response.json()["payload"] == "User not exist"


def test_fail_unauthorized_user(client: TestClient):
    user_id = 100
    response = client.delete(f"{const.API_PREFIX}/{user_id}")
    assert response.status_code == 401
    assert "detail" in response.json().keys()
