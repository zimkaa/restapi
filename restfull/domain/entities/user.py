from typing import Any

from .entity import Entity


class BaseModel(Entity):
    id: int

    def to_dict(self) -> dict[str, Any]:
        return self.model_dump()
    

class User(Entity):
    first_name: str
    last_name: str


class BaseUser(BaseModel, User):
    ...
