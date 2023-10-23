from typing import Any

from .entity import Entity


class BaseUser(Entity):
    id: int
    first_name: str
    last_name: str

    def to_dict(self) -> dict[str, Any]:
        return self.model_dump()
