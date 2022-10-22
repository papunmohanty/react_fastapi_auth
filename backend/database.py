from sqlite3 import connect

import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

DATABASE_URI = "sqlite:///./database.db"

engine = _sql.create_engine(
    DATABASE_URI, connect_args={"check_same_thread": False}
)

SessionLocal = _orm.sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

Base = _declarative.declarative_base()
