from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import BIGINT, VARCHAR, func, ForeignKey
from sqlalchemy.dialects.postresql import TIMESTAMP
import datetime


class Base(DeclarativeBase):
    pass


# 1.- Create a Table
# 2.- Creating columns
# 3.- SQL data types
# 4.- Primary key
# 5.- NUll Constraints
# 6.- Default value
# 7.- Foreign keys
# 8.- SQL Expressions
# 9.- Functions in SQLAlchemy
# 10.- Naming a table


class User(Base):
    __tablename__ = "users"

    telegram_id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    full_name: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    username: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    language_code: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, nullable=False, server_default=func.now()
    )
    referred_id: Mapped[int] = mapped_column(
        BIGINT, ForeignKey("users.telegram_id", ondelete="SET NULL"), nullable=False
    )
