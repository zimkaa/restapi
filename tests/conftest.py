import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from restfull.domain import const
from restfull.domain.entities.user import BaseUserWhitPassword
from restfull.infrastructure.api.application import application
from restfull.infrastructure.config import settings
from restfull.infrastructure.database.sqlalchemy import create_session
from restfull.infrastructure.models import Base


@pytest.fixture
def default_user() -> BaseUserWhitPassword:
    return BaseUserWhitPassword(id=1, name="Anna")

test_engine = create_async_engine(
    settings.test_database_url,
    echo=True,
)


async def _create_session_test():
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    return async_sessionmaker(test_engine, expire_on_commit=False)


@pytest.fixture(scope="function")
def client() -> TestClient:
    application.dependency_overrides[create_session] = _create_session_test
    return TestClient(application)


@pytest.fixture
def create_user(client: TestClient, default_user: BaseUserWhitPassword):
    client.post(const.API_PREFIX, json=default_user.to_dict())


@pytest.fixture
def create_user_and_teardown(client: TestClient, default_user: BaseUserWhitPassword):
    client.post(const.API_PREFIX, json=default_user.to_dict())
    yield
    client.delete(f"{const.API_PREFIX}/{default_user.id}")


@pytest.fixture
def delete_default_user(client: TestClient, default_user: BaseUserWhitPassword):
    yield
    client.delete(f"{const.API_PREFIX}/{default_user.id}")
