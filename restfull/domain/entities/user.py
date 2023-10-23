from .entity import Entity


class BaseModel(Entity):
    id: int


class User(Entity):
    name: str
    last_name: str
    email: str


class UserWhitPassword(User):
    password: str


class BaseUser(BaseModel, User):
    ...


class BaseUserWhitPassword(BaseUser):
    password: str
