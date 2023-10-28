from typing import Optional

from fastapi import Depends
from fastapi import Request
from fastapi_users import BaseUserManager
from fastapi_users import IntegerIDMixin

from restfull.infrastructure.config import settings
from restfull.infrastructure.database.sqlalchemy import get_user_db
from restfull.infrastructure.models.user import UserModel


SECRET = settings.manager_secret


class UserManager(IntegerIDMixin, BaseUserManager[UserModel, int]):  # type: ignore
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: UserModel, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
