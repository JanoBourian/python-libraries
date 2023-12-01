## Dependencies

```bash
pip install psycopg2-binary asyncpg sqlalchemy
```

## Docker container for PostgreSQL

```bash
docker run --name pgconnection -e POSTGRES_PASSWORD=password -e POSTGRES_USER=postgres -e POSTGRES_DB=postgres -p 5433:5432 -d postgres:13.4-alpine
netstat -ano | find ":5433"
```

## Way to create tables using row sql

```python
# with engine.connect() as connection:
#     connection.execute(text('SELECT 1'))

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
```

## Steps to create Tables

1.- Create a table in SQLAlchemy
2.- Create columns
3.- SQL Data Types
4.- Primary keys
5.- Null constraints
6.- Default values
7.- Foreign keys
8.- SQL Expressions
9.- Functions in SQLAlchemy
10.- Naming a Table