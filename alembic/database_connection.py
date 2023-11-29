from sqlalchemy import create_engine, URL, text
from sqlalchemy.orm import sessionmaker

# connection string format: driver+postgresql://user:pass@host:port/dbname
DATABASE_URL = URL.create(
    drivername = "postgresql+psycopg2",
    username = "postgres",
    password = "password",
    host = "localhost",
    port = 5433,
    database = "postgres"
)
engine = create_engine(DATABASE_URL, echo=True)

# with engine.connect() as connection:
#     connection.execute(text('SELECT 1'))
    

session_pool = sessionmaker(engine)

with session_pool() as session:
    session.execute(text('SELECT 1;'))
    session.commit()
    session.rollback()