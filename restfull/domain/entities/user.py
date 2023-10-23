from .entity import Entity


class BaseModel(Entity):
    id: int
    

class User(Entity):
    name: str
    last_name: str
    email: str
    password: str


class BaseUser(BaseModel, User):
    ...
