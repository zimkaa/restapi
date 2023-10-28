from fastapi.testclient import TestClient

from restfull.domain import const
from restfull.infrastructure.auth.schemas import UserCreate


def test_get_user_by_id(client: TestClient, default_user_create: UserCreate, create_user):
    default_user_id = 1
    response = client.get(f"{const.API_PREFIX}/{default_user_id}")
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()["payload"]["name"] == default_user_create.name
    assert response.json()["payload"]["last_name"] == default_user_create.last_name
    assert response.json()["payload"]["email"] == default_user_create.email


def test_fail_get_user_by_id(client: TestClient):
    default_user_id = 1
    response = client.get(f"{const.API_PREFIX}/{default_user_id}")
    assert response.status_code == 404
    assert response.json()["result"] == "error"
