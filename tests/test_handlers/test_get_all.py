from fastapi.testclient import TestClient

from restfull.domain import const


def test_get_all_users(client: TestClient, create_user_and_teardown):
    response = client.get(const.API_PREFIX)
    assert response.status_code == 200
    assert len(response.json()) > 0
