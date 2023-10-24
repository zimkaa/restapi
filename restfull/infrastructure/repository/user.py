from loguru import logger
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker

from restfull.domain.entities.user import BaseUser
from restfull.domain.entities.user import UserWhitPassword
from restfull.domain.repository.user import UserRepository
from restfull.domain.types import UserID
from restfull.infrastructure.models.user import UserModel


def from_model_to_base_user(model: UserModel) -> BaseUser:
    return BaseUser(
        id=model.id,
        name=model.name,
        last_name=model.last_name,
        email=model.email if model.email else "",
    )


class UserRepositorySqlalchemy(UserRepository):
    def __init__(self, database: async_sessionmaker[AsyncSession]):
        self.database = database

    async def create(self, user: UserWhitPassword) -> bool:
        async with self.database() as session:
            user_dict = user.to_dict()
            query = text(
                "INSERT INTO users (name, last_name, email, password) VALUES (:name, :last_name, :email, :password)"
            )
            query = query.bindparams(**user_dict)
            try:
                await session.execute(query)
            except Exception as exc:
                logger.error(exc)
                raise exc
            await session.commit()

        return True

    async def get_by_id(self, user_id: UserID) ->  BaseUser | None:
        async with self.database() as session:
            query = text("SELECT * FROM users WHERE id=:id")
            query = query.bindparams(id=user_id)
            result = await session.execute(query)

        user_model = result.fetchone()
        if user_model:
            return from_model_to_base_user(user_model)
        return None

    async def get_all(self) -> list[BaseUser]:
        async with self.database() as session:
            query = text("SELECT * FROM users")
            result = await session.execute(query)

        return [from_model_to_base_user(user_model) for user_model in result.fetchall()]

    async def update(self, user: BaseUser) -> BaseUser | None:
        async with self.database() as session:
            user_dict = user.to_dict()
            query = text(
                "UPDATE users SET name=:name, last_name=:last_name, email=:email, password=:password WHERE id=:id"
            )
            query = query.bindparams(**user_dict)
            try:
                result = await session.execute(query)
            except Exception as exc:
                logger.error(exc)
                raise exc
            await session.commit()

        if result.rowcount == 0:
            return None
        return user

    async def delete(self, user_id: UserID) -> bool:
        async with self.database() as session:
            query = text("DELETE FROM users WHERE id=:id")
            query = query.bindparams(id=user_id)
            try:
                result = await session.execute(query)
            except Exception as exc:
                logger.error(exc)
                raise exc
            await session.commit()

        if result.rowcount == 0:
            return False
        return True

    async def search_user_by_name(self, name: str) -> list[BaseUser]:
        async with self.database() as session:
            query = text("SELECT * FROM users WHERE name=:username")
            query = query.bindparams(username=name)
            result = await session.execute(query)

        return [from_model_to_base_user(user_model) for user_model in result.fetchall()]
