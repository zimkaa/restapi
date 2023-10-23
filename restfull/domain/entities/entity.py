from typing import Any

from pydantic import BaseModel


class Entity(BaseModel):
    class Config:
        from_attributes = True

    def to_dict(self) -> dict[str, Any]:
        return self.model_dump()
