from abc import ABC
from abc import abstractmethod

from restfull.domain.entities.user import BaseUser
from restfull.domain.types import UserID


class UserRepository(ABC):
    """Data Access Layer for user info"""

    @abstractmethod
    async def get_by_id(self, user_id: UserID) -> BaseUser | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_all(self) -> list[BaseUser]:
        raise NotImplementedError()

    @abstractmethod
    async def update(self, user: BaseUser) -> BaseUser | None:
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, user_id: UserID) -> bool:
        raise NotImplementedError()

    @abstractmethod
    async def search_user_by_name(self, name: str) -> list[BaseUser]:
        raise NotImplementedError()
