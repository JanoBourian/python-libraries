from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import BIGINT, VARCHAR, func, ForeignKey, Column, UUID, TIMESTAMP
from sqlalchemy.ext.declarative import declared_attr
import datetime


class Base(DeclarativeBase):
    pass


class TableNameMixin(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower() + "s"

    id = Column(UUID, primary_key=True)


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, nullable=False, server_default=func.now(), onupdate=func.now()
    )


class User(TableNameMixin, Base, TimestampMixin):
    full_name: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    username: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    language_code: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    referred_id: Mapped[int] = mapped_column(
        UUID, ForeignKey("users.id", ondelete="SET NULL"), nullable=False
    )


class Product(TableNameMixin, Base, TimestampMixin):
    title: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    description: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)


class Order(TableNameMixin, Base, TimestampMixin):
    user_id: Mapped[UUID] = mapped_column(
        UUID, ForeignKey("users.id", ondelete="SET NULL"), nullable=False
    )


class OrderProduct(TableNameMixin, Base, TimestampMixin):
    order_id: Mapped[UUID] = mapped_column(
        UUID, ForeignKey("orders.id", ondelete="CASCADE"), nullable=False
    )
    product_id: Mapped[UUID] = mapped_column(
        UUID, ForeignKey("products.id", ondelete="RESTRICT"), nullable=False
    )
    quantity: Mapped[int] = mapped_column(BIGINT, nullable=False)

    # order = relationship("Order", back_populates = "orderproducts")
    # product = relationship("Product", back_populates = "orderproducts")
