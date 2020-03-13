import sys
from loguru import logger
import psycopg2


class Database:
    """PostgreSQL Database class."""

    def __init__(self, config):
        self.host = config.DATABASE_HOST
        self.username = config.DATABASE_USERNAME
        self.password = config.DATABASE_PASSWORD
        self.port = config.DATABASE_PORT
        self.dbname = config.DATABASE_NAME
        self.conn = None

    def open_connection(self):
        """Connect to a Postgres database."""
        if self.conn is None:
            try:
                self.conn = psycopg2.connect(host=self.host,
                                             user=self.username,
                                             password=self.password,
                                             port=self.port,
                                             dbname=self.dbname)
            except psycopg2.DatabaseError as e:
                logger.error(e)
                sys.exit()
            finally:
                logger.info('Connection opened successfully.')

    def select_rows(self, query):
        """Run a SQL query to select rows from table."""
        self.open_connection()
        with self.conn.cursor() as cur:
            cur.execute(query)
            records = [row for row in cur.fetchall()]
            cur.close()
            return records

    def update_rows(self, query):
        """Run a SQL query to update rows in table."""
        self.open_connection()
        with self.conn.cursor() as cur:
            cur.execute(query)
            self.conn.commit()
            cur.close()
            return f"{cur.rowcount} rows affected."
