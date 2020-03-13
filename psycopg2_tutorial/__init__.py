from config import Config
from .db import Database
from .queries import read_sql_from_files
import pprint


def run_script():
    """Execute queries against PostgreSQL database."""
    pp = pprint.PrettyPrinter(indent=1)
    db = Database(Config)
    queries = read_sql_from_files(Config.SQL_QUERIES_FOLDER)
    results = [db.select_rows(query) for query in queries]
    pp.pprint(results)
    return results
