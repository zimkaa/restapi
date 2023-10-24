from fastapi.testclient import TestClient

from restfull.domain import const
from restfull.domain.entities.user import UserWhitPassword
from restfull.infrastructure.api.endpoints.search_user import ErrorNoUsersResponse
from restfull.infrastructure.api.endpoints.search_user import ErrorParameterResponse


def test_search_user(client: TestClient, create_user_and_teardown):
    test_user = UserWhitPassword(name="Anna")
    response = client.get(f"{const.API_PREFIX}/?name={test_user.name}")
    assert response.status_code == 200
    for user in response.json()["payload"]:
        assert user["name"] == test_user.name


def test_fail_search_user(client: TestClient):
    response = client.get(f"{const.API_PREFIX}/?name=100")
    assert response.status_code == 404
    assert response.json() == ErrorNoUsersResponse().model_dump()
    assert response.json()["result"] == "error"
    assert response.json()["payload"] == "Users with that name not exist"


def test_fail_search_user_without_params(client: TestClient):
    response = client.get(f"{const.API_PREFIX}/?name=")
    assert response.status_code == 406
    assert response.json() == ErrorParameterResponse().model_dump()
    assert response.json()["result"] == "error"
    assert response.json()["payload"] == "Name query param doesn't exist"
