from fastapi.testclient import TestClient

from restfull.domain import const
from restfull.domain.entities.user import BaseUserWhitPassword


def test_get_all_users(client: TestClient, default_user: BaseUserWhitPassword, create_user_and_teardown):
    response = client.get(const.API_PREFIX)
    assert response.status_code == 200
    assert len(response.json()) > 0
    for user in response.json():
        assert user["id"] == default_user.id
