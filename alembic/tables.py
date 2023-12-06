from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import BIGINT


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
