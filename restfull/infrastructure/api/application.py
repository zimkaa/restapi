from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from restfull.infrastructure.api.endpoints import get_all_users
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
    prefix=f"/{const.ALL_USERS}",
    tags=[const.USER_TAG],
)
