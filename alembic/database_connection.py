from sqlalchemy import create_engine, URL, text
from sqlalchemy.orm import sessionmaker
from configuration import env

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

# with engine.connect() as connection:
#     connection.execute(text('SELECT 1'))


session_pool = sessionmaker(engine)
# with session_pool() as session:
#     session.execute(
#         text(
#             """
#                          CREATE TABLE users(
#                              telegram_id BIGINT PRIMARY KEY,
#                              fullname VARCHAR(255) NOT NULL,
#                              username VARCHAR(255) NOT NULL,
#                              language_code VARCHAR(255) NOT NULL,
#                              created_at TIMESTAMP DEFAULT NOW(),
#                              referred_id BIGINT,
#                              FOREIGN KEY (referred_id) 
#                              REFERENCES users (telegram_id)
#                              ON DELETE SET NULL
#                          )
#                          """
#         )
#     )
#     session.execute(
#         text(
#             """
#                          INSERT INTO users (
#                              telegram_id,
#                              fullname,
#                              username,
#                              language_code
#                              ) 
#                          VALUES (
#                              1,
#                              'Minerva',
#                              'minerva37',
#                              'en'
#                          )
#                          """
#         )
#     )
#     session.execute(
#         text(
#             """
#                          INSERT INTO users (
#                              telegram_id,
#                              fullname,
#                              username,
#                              language_code,
#                              referred_id
#                              ) 
#                          VALUES (
#                              2,
#                              'Jano Bourian',
#                              'janobourian',
#                              'en',
#                              1
#                          )
#                          """
#         )
#     )
#     session.commit()

with session_pool() as session:
    results = session.execute(text("""
                                  SELECT * FROM users;"""))
    for row in results:
        print(row)
