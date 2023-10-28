from abc import ABC
from abc import abstractmethod

from restfull.domain.entities.user import BaseUser
from restfull.domain.entities.user import User
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
    async def update(self, user_id: UserID) -> BaseUser:
        raise NotImplementedError()
    
    @abstractmethod
    async def delete(self, user_id: UserID) -> BaseUser | None:
        raise NotImplementedError()
    
    @abstractmethod
    async def search_user_by_name(self, name: str) -> BaseUser | None:
        raise NotImplementedError()
