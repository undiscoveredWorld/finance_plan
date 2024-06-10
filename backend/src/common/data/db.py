import settings

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    f"postgresql+psycopg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}" +
    f"@{settings.POSTGRES_HOST}/{settings.POSTGRES_DB}",
)
Base = declarative_base()
Session = sessionmaker(engine)


def get_session() -> Session:
    session = Session()
    try:
        return session
    finally:
        session.close()
