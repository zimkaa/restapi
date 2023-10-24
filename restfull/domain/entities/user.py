from restfull.domain import const

from .entity import Entity


class BaseModel(Entity):
    id: int


class User(Entity):
    name: str = const.EXAMPLE_NAME
    last_name: str = const.EXAMPLE_LAST_NAME
    email: str = const.EXAMPLE_EMAIL


class UserWhitPassword(User):
    password: str = const.EXAMPLE_PASSWORD


class BaseUser(BaseModel, User):
    ...


class BaseUserWhitPassword(BaseUser):
    password: str = const.EXAMPLE_PASSWORD
