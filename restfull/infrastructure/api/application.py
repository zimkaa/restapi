from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from restfull.domain import const
from restfull.infrastructure.api.endpoints import auth
from restfull.infrastructure.api.endpoints import delete_user
from restfull.infrastructure.api.endpoints import get_all_users
from restfull.infrastructure.api.endpoints import get_user
from restfull.infrastructure.api.endpoints import search_user
from restfull.infrastructure.api.endpoints import update_user
from restfull.infrastructure.config import settings


app = FastAPI(
    title=settings.project_name,
    version=settings.app_version,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    auth.auth_user,
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    auth.register_user,
    prefix="/api",
    tags=[const.USER_TAG],
)

app.include_router(
    get_all_users.router,
    prefix=const.API_PREFIX,
    tags=[const.USER_TAG],
)

app.include_router(
    get_user.router,
    prefix=const.API_PREFIX,
    tags=[const.USER_TAG],
)

app.include_router(
    update_user.router,
    prefix=const.API_PREFIX,
    tags=[const.USER_TAG],
)

app.include_router(
    delete_user.router,
    prefix=const.API_PREFIX,
    tags=[const.USER_TAG],
)

app.include_router(
    search_user.router,
    prefix=const.API_PREFIX,
    tags=[const.USER_TAG],
)
