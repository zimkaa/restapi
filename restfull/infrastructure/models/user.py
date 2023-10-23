from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from restfull.infrastructure.models import Model


class UserModel(Model):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=False)
