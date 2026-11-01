import os

import psycopg2

# Optional: load DB_* settings from a local .env file if python-dotenv is installed.
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


def _setting(name, default=None):
    """Read a setting from environment variables, then from Streamlit secrets."""
    value = os.getenv(name)
    if value is not None:
        return value
    try:
        import streamlit as st
        return st.secrets.get(name, default)
    except Exception:
        return default


def connection():
    password = _setting("DB_PASSWORD")
    if password is None:
        raise RuntimeError(
            "DB_PASSWORD is not set. Add it to .env locally, or to the app's Secrets on Streamlit Cloud."
        )

    con = psycopg2.connect(
        host=_setting("DB_HOST", "localhost"),
        database=_setting("DB_NAME", "ecommerce"),
        user=_setting("DB_USER", "postgres"),
        password=password,
        port=_setting("DB_PORT", "5432"),
        sslmode=_setting("DB_SSLMODE", "prefer"),
    )

    if con:
        print(">>>>> Connection Established !")
    else:
        print(">>>>> Connection Failed !")
    return con