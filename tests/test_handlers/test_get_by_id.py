from fastapi.testclient import TestClient

from restfull.domain import const
from restfull.domain.entities.user import BaseUserWhitPassword


def test_get_user_by_id(client: TestClient, default_user: BaseUserWhitPassword, create_user_and_teardown):
    response = client.get(f"{const.API_PREFIX}/{default_user.id}")
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()["name"] == default_user.name
    assert response.json()["last_name"] == default_user.last_name
    assert response.json()["email"] == default_user.email
