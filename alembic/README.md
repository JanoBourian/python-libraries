## Dependencies

```bash
pip install psycopg2-binary asyncpg sqlalchemy
```

## Docker container for PostgreSQL

```bash
docker run --name pgconnection -e POSTGRES_PASSWORD=password -e POSTGRES_USER=postgres -e POSTGRES_DB=postgres -p 5433:5432 -d postgres:13.4-alpine
netstat -ano | find ":5433"
```