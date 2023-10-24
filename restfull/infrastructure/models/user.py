from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import null
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from restfull.domain.types import UserID
from restfull.infrastructure.models import Base


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[UserID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=True, server_default=null())
    password: Mapped[str] = mapped_column(String, nullable=True, server_default=null())
