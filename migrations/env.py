from logging.config import fileConfig
from alembic import context as ctx
from sqlalchemy import create_engine
from bookshelf.db_set.db_accessor import db
from config import DATABASE_URL


config = ctx.config
fileConfig(config.config_file_name)
target_metadata = db

def run_migrations_online():
    database_url = DATABASE_URL
    connectable = create_engine(database_url)
    with connectable.connect() as connection:
        ctx.configure(connection=connection, target_metadata=target_metadata)
        with ctx.begin_transaction():
            ctx.run_migrations()

run_migrations_online()
