from fastapi_users.authentication import AuthenticationBackend
from fastapi_users.authentication import CookieTransport
from fastapi_users.authentication import JWTStrategy

from restfull.infrastructure.config import settings


cookie_transport = CookieTransport(cookie_name=settings.project_name, cookie_max_age=3600)

SECRET = settings.jwt_secret


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
