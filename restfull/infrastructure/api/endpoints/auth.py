from fastapi_users import FastAPIUsers

from restfull.infrastructure.auth.auth import auth_backend
from restfull.infrastructure.auth.manager import get_user_manager
from restfull.infrastructure.auth.schemas import UserCreate
from restfull.infrastructure.auth.schemas import UserRead
from restfull.infrastructure.models.user import UserModel


fastapi_users = FastAPIUsers[UserModel, int](  # type: ignore
    get_user_manager,
    [auth_backend],
)
auth_user = fastapi_users.get_auth_router(auth_backend)

register_user = fastapi_users.get_register_router(UserRead, UserCreate)

current_user = fastapi_users.current_user()
