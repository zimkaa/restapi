from loguru import logger
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

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
    def __init__(self, database: AsyncSession):
        self.session = database

    async def create(self, user: UserWhitPassword) -> bool:
        user_dict = user.to_dict()
        query = text(
            "INSERT INTO users (name, last_name, email) VALUES (:name, :last_name, :email)"
        )
        query = query.bindparams(**user_dict)
        try:
            await self.session.execute(query)
        except Exception as exc:
            logger.error(exc)
            raise exc
        await self.session.commit()

        return True

    async def get_by_id(self, user_id: UserID) ->  BaseUser | None:
        query = text("SELECT * FROM users WHERE id=:id")
        query = query.bindparams(id=user_id)
        result = await self.session.execute(query)

        user_model = result.fetchone()
        if user_model:
            return from_model_to_base_user(user_model)
        return None

    async def get_all(self) -> list[BaseUser]:
        query = text("SELECT * FROM users")
        result = await self.session.execute(query)

        return [from_model_to_base_user(user_model) for user_model in result.fetchall()]

    async def update(self, user: BaseUser) -> BaseUser | None:
        user_dict = user.to_dict()
        query = text(
            "UPDATE users SET name=:name, last_name=:last_name, email=:email WHERE id=:id"
        )
        query = query.bindparams(**user_dict)
        try:
            result = await self.session.execute(query)
        except Exception as exc:
            logger.error(exc)
            raise exc
        await self.session.commit()

        if result.rowcount == 0:
            return None
        return user

    async def delete(self, user_id: UserID) -> bool:
        query = text("DELETE FROM users WHERE id=:id")
        query = query.bindparams(id=user_id)
        try:
            result = await self.session.execute(query)
        except Exception as exc:
            logger.error(exc)
            raise exc
        await self.session.commit()

        if result.rowcount == 0:
            return False
        return True

    async def search_user_by_name(self, name: str) -> list[BaseUser]:
        query = text("SELECT * FROM users WHERE name=:username")
        query = query.bindparams(username=name)
        result = await self.session.execute(query)

        return [from_model_to_base_user(user_model) for user_model in result.fetchall()]
