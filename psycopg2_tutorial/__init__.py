from config import Config
from .db import Database
from .queries import read_sql_from_files


def run_script():
    """Execute queries against PostgreSQL database."""
    db = Database(Config)
    queries = read_sql_from_files(Config.SQL_QUERIES_FOLDER)
    results = [db.select_rows(query) for query in queries]
    return results
