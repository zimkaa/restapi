from fastapi.testclient import TestClient

from restfull.domain import const
from restfull.domain.entities.user import UserWhitPassword
from restfull.infrastructure.api.endpoints.create_user import ErrorBodyParameterResponse
from restfull.infrastructure.api.responses.base import OkResponse


def test_create_user(client: TestClient, delete_default_user):
    test_user = UserWhitPassword(name="Helen")
    response = client.post(const.API_PREFIX, json=test_user.to_dict())
    assert response.status_code == 200
    assert response.json() == OkResponse().model_dump()


def test_fail_create_user(client: TestClient):
    test_user = UserWhitPassword()
    response = client.post(const.API_PREFIX, json=test_user.to_dict())
    assert response.status_code == 406
    assert response.json() == ErrorBodyParameterResponse().model_dump()
