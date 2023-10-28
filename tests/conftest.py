import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from restfull.infrastructure.api.application import app
from restfull.infrastructure.auth.schemas import UserCreate
from restfull.infrastructure.config import settings
from restfull.infrastructure.database.sqlalchemy import get_async_session
from restfull.infrastructure.models.base import Base


@pytest.fixture
def default_user_create() -> UserCreate:
    default_user = UserCreate(
        email="test@example.com",
        password="testpassword",
        is_active=True,
        is_superuser=False,
        is_verified=False,
        name="testuser",
        last_name="testlastname",
    )
    return default_user


engine_test = create_async_engine(
    settings.test_database_url,
    echo=True,
)
async_session_maker = async_sessionmaker(engine_test, expire_on_commit=False)


async def _get_async_session_test():
    async with async_session_maker() as session:
        yield session


app.dependency_overrides[get_async_session] = _get_async_session_test


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture(autouse=True, scope="function")
async def prepare_database():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture
def create_user(client: TestClient, default_user_create: UserCreate):
    client.post("/api/register", json=default_user_create.model_dump())


@pytest.fixture
def authorize_cookie(client: TestClient, create_user, default_user_create: UserCreate):
    response = client.post(
        "/auth/jwt/login",
        data={"username": default_user_create.email, "password": default_user_create.password},
    )
    return {"restfull": response.cookies["restfull"]}
