"""Script entry point."""
from config import (
    DATABASE_HOST,
    DATABASE_USERNAME,
    DATABASE_PASSWORD,
    DATABASE_PORT,
    DATABASE_NAME,
)
from .db import Database
from .queries import queries
from .log import LOGGER

# Create database class
db = Database(
    DATABASE_HOST,
    DATABASE_USERNAME,
    DATABASE_PASSWORD,
    DATABASE_PORT,
    DATABASE_NAME
)


def init_script():
    """Execute queries against PostgreSQL database."""
    standard_results = db.select_rows(queries[0])
    dict_cursor_results = db.select_rows_dict_cursor(queries[0])
    display_query_results(standard_results, cursor_type='standard')
    display_query_results(dict_cursor_results, cursor_type='dictcursor')


def display_query_results(rows, cursor_type=None):
    """Log results of query to console."""
    LOGGER.info(f'Results from {cursor_type}:')
    for row in rows:
        LOGGER.info(row)
