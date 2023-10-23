from fastapi.testclient import TestClient

from restfull.domain import const
from restfull.domain.entities.user import UserWhitPassword
from restfull.infrastructure.api.application import application

client = TestClient(application)

test_user = UserWhitPassword().to_dict()


def test_create_user():
    response = client.post(const.API_PREFIX, json=test_user)
    assert response.status_code == 200
    assert response.json() == True
