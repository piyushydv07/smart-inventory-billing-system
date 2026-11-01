import os

import psycopg2

# Optional: load DB_* settings from a local .env file if python-dotenv is installed.
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


def connection():
    password = os.getenv("DB_PASSWORD")
    if password is None:
        raise RuntimeError(
            "DB_PASSWORD is not set. Copy .env.example to .env and fill in your PostgreSQL password."
        )

    con = psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "ecommerce"),
        user=os.getenv("DB_USER", "postgres"),
        password=password,
        port=os.getenv("DB_PORT", "5432"),
    )

    if con:
        print(">>>>> Connection Established !")
    else:
        print(">>>>> Connection Failed !")
    return con
