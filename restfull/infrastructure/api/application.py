from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from restfull.infrastructure.api.endpoints import get_all_users
from restfull.infrastructure.config import settings


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
    prefix=f"/{settings.all_users}",
    tags=[settings.user_tag],
)
