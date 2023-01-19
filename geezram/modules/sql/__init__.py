from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from geezram import DB_URL


def start() -> scoped_session:
    engine = create_engine("postgresql://myoytwcspxphxh:9efe912049e6570d5b1b5d5863ec9f5785662be26fb6f5d0c56b0b5f59fad3ac@ec2-54-90-13-87.compute-1.amazonaws.com:5432/d5eddak9q11n4q")
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=True))


BASE = declarative_base()
SESSION = start()
