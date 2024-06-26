from os import environ
from dotenv import load_dotenv

load_dotenv("docker.env")

POSTGRES_PASSWORD = environ["POSTGRES_PASSWORD"]
POSTGRES_USER = environ["POSTGRES_USER"]
POSTGRES_DB = environ["POSTGRES_DB"]
POSTGRES_HOST = environ.get("POSTGRES_HOST") or "localhost"

REDIS_HOST = environ.get("REDIS_HOST") or "localhost"
REDIS_PORT = environ.get("REDIS_PORT") or 6379

CACHING_KEYS = {
    "categories": "categories",
    "subcategories": "subcategories",
    "buys": "buys"
}