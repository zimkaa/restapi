from fastapi.testclient import TestClient

from restfull.domain import const
from restfull.domain.entities.user import UserWhitPassword


def test_search_user(client: TestClient, create_user_and_teardown):
    test_user = UserWhitPassword()
    response = client.get(f"{const.API_PREFIX}/?name={test_user.name}")
    assert response.status_code == 200
    for user in response.json():
        assert user["name"] == test_user.name
