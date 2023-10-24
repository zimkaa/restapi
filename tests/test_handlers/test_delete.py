from fastapi.testclient import TestClient

from restfull.domain import const
from restfull.infrastructure.api.endpoints.delete_user import ErrorNoUserResponse
from restfull.infrastructure.api.responses.base import OkResponse


user_id = 1


def test_delete_user(client: TestClient, create_user):
    response = client.delete(f"{const.API_PREFIX}/{user_id}")
    assert response.status_code == 200
    assert response.json() == OkResponse().model_dump()


def test_fail_delete_user(client: TestClient):
    response = client.delete(f"{const.API_PREFIX}/{user_id}")
    assert response.status_code == 404
    assert response.json() == ErrorNoUserResponse().model_dump()
    assert response.json()["result"] == "error"
    assert response.json()["payload"] == "User not exist"
