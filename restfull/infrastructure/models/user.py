from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import Boolean
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from restfull.domain.types import UserID
from restfull.infrastructure.models import Base


class UserModel(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "users"

    id: Mapped[UserID] = mapped_column(primary_key=True)  # type: ignore
    name: Mapped[str] = mapped_column(String, nullable=False)  # type: ignore
    last_name: Mapped[str] = mapped_column(String, nullable=False)  # type: ignore
    email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=False)  # type: ignore
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)  # type: ignore
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)  # type: ignore
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)  # type: ignore
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)  # type: ignore
