from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from restfull.infrastructure.api.endpoints import get_all_users
from restfull.infrastructure.api.endpoints import create_user
from restfull.infrastructure.api.endpoints import get_user
from restfull.infrastructure.api.endpoints import update_user
from restfull.infrastructure.api.endpoints import delete_user
from restfull.infrastructure.api.endpoints import search_user
from restfull.infrastructure.config import settings
from restfull.domain import const


application = FastAPI(
    title=settings.project_name,
    version=settings.app_version,
)

application.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

application.include_router(
    get_all_users.router,
    prefix=const.API,
    tags=[const.USER_TAG],
)

application.include_router(
    get_user.router,
    prefix=const.API,
    tags=[const.USER_TAG],
)

application.include_router(
    create_user.router,
    prefix=const.API,
    tags=[const.USER_TAG],
)

application.include_router(
    update_user.router,
    prefix=const.API,
    tags=[const.USER_TAG],
)

application.include_router(
    delete_user.router,
    prefix=const.API,
    tags=[const.USER_TAG],
)

application.include_router(
    search_user.router,
    prefix=const.API,
    tags=[const.USER_TAG],
)
