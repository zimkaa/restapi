from fastapi.testclient import TestClient

from restfull.domain import const


user_id = 1


def test_delete_user(client: TestClient, create_user):
    response = client.delete(f"{const.API_PREFIX}/{user_id}")
    assert response.status_code == 200
    assert response.json() == {"ok": "user deleted"}


def test_fail_delete_user(client: TestClient):
    response = client.delete(f"{const.API_PREFIX}/{user_id}")
    assert response.status_code == 200
    assert response.json() == {"error": "some error"}
