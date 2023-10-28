from fastapi.testclient import TestClient

from restfull.infrastructure.auth.schemas import UserCreate


def test_register_user(client: TestClient, default_user_create: UserCreate):
    user_json = default_user_create.model_dump()
    response = client.post(
        "/api/register",
        json=user_json,
    )
    assert response.status_code == 201


def test_login(client: TestClient, default_user_create: UserCreate, create_user):
    response = client.post(
        "/auth/jwt/login",
        data={"username": default_user_create.email, "password": default_user_create.password},
    )
    assert response.status_code == 204
