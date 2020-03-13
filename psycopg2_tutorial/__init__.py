from config import Config
from .db import Database
from .queries import read_sql_from_files
from loguru import logger

db = Database(Config)  # Create database class
queries = read_sql_from_files(Config.SQL_QUERIES_FOLDER)  # Fetch queries from local files


def init_script():
    """Execute queries against PostgreSQL database."""
    standard_results = db.select_rows(queries[0])
    dictcursor_results = db.select_rows_dict_cursor(queries[0])
    display_query_results(standard_results, 'psycopg2 standard cursor')
    display_query_results(dictcursor_results, 'psycopg2 dictcursor')


def display_query_results(rows, type):
    logger.info(f'Results from {type}:')
    for row in rows:
        logger.info(row)
