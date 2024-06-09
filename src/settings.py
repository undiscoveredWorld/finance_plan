from os import environ
from dotenv import load_dotenv

load_dotenv("docker.env")

POSTGRES_PASSWORD = environ["POSTGRES_PASSWORD"]
POSTGRES_USER = environ["POSTGRES_USER"]
POSTGRES_DB = environ["POSTGRES_DB"]
POSTGRES_HOST = environ.get("POSTGRES_HOST") or "localhost"
