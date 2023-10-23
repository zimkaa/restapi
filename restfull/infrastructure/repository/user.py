from loguru import logger
# from sqlalchemy import delete
from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from restfull.domain.entities.user import BaseUser, User
from restfull.domain.repository.user import UserRepository
from restfull.domain.types import UserID
from restfull.infrastructure.models.user import UserModel


def from_model_to_base_user(model: UserModel) -> BaseUser:
    return BaseUser(
        id=model.id,
        name=model.name,
        last_name=model.last_name,
        email=model.email if model.email else "",
        password=model.password if model.password else "",
    )


class UserRepositorySqlalchemy(UserRepository):
    def __init__(self, database: async_sessionmaker[AsyncSession]):
        self.database = database

    async def create(self, user: User) -> bool:
        async with self.database() as session:
            user_dict = user.to_dict()
            # TODO: pure SQL
            query = insert(UserModel).values(**user_dict)
            try:
                await session.execute(query)
            except Exception as exc:
                logger.error(exc)
                raise exc
            await session.commit()

        return True

    async def get_by_id(self, user_id: UserID) ->  BaseUser | None:
        async with self.database() as session:
            # TODO: pure SQL
            query = select(UserModel).where(UserModel.id == user_id)
            result = await session.scalars(query)

        user_model = result.one_or_none()
        if user_model:
            return from_model_to_base_user(user_model)
        return None

    async def get_all(self) -> list[BaseUser]:
        async with self.database() as session:
            # TODO: pure SQL
            query = select(UserModel)
            result = await session.scalars(query)

        return [from_model_to_base_user(user_model) for user_model in result.unique().all()]

    async def update(self, user: BaseUser) -> BaseUser:
        async with self.database() as session:
            user_dict = user.to_dict()
            # TODO: pure SQL
            query = update(UserModel).where(UserModel.id == user.id).values(**user_dict)
            try:
                await session.execute(query)
            except Exception as exc:
                logger.error(exc)
                raise exc
            await session.commit()

        return user

    async def delete(self, user_id: UserID) -> bool:
        async with self.database() as session:
            # TODO: pure SQL
            # query = delete(UserModel).where(UserModel.id == user_id)
            query = text(f"DELETE FROM users WHERE id = {user_id};")
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
            # TODO: pure SQL
            query = select(UserModel).where(UserModel.name == name)
            result = await session.execute(query)

        return [from_model_to_base_user(user_model) for user_model in result.scalars().all()]
