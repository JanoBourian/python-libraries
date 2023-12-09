from sqlalchemy import create_engine, URL, text
from sqlalchemy.orm import sessionmaker
from configuration import env
from tables import Base, User, Product, Order, OrderProduct

# connection string format: driver+postgresql://user:pass@host:port/dbname
DATABASE_URL = URL.create(
    drivername=env("DRIVERNAME"),
    username=env("DBUSERNAME"),
    password=env("PASSWORD"),
    host=env("HOST"),
    port=env("PORT"),
    database=env("DATABASE"),
)
engine = create_engine(DATABASE_URL, echo=True)
Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)
# session_pool = sessionmaker(engine)
