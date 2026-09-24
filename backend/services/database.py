import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text


# Load variables from .env
load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")


if not DATABASE_URL:
    raise RuntimeError(
        "DATABASE_URL is not configured. "
        "Please create a .env file in the project root."
    )


# Create SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)


def test_database_connection():
    """
    Test whether the application can connect to MySQL.
    """

    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return True

    except Exception as error:
        print(f"Database connection failed: {error}")
        return False