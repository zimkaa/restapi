from fastapi.testclient import TestClient

from restfull.domain import const
from restfull.domain.entities.user import BaseUserWhitPassword


def test_get_user_by_id(client: TestClient, create_user_and_teardown, default_user: BaseUserWhitPassword):
    response = client.get(f"{const.API_PREFIX}/1")
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()["id"] == default_user.id
