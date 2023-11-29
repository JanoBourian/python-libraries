## Dependencies

```bash
pip install psycopg2-binary asyncpg sqlalchemy
```

## Docker container for PostgreSQL

```bash
docker run --name postgresqlalembic -e POSTGRES_PASSWORD=password -e POSTGRES_USER=user -e POSTGRES_DB=test -p 5432:5432 -d postgres:13.4-alpine
```