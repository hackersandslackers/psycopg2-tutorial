import sys
import logging
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
        try:
            self.conn = psycopg2.connect(host=self.host,
                                         user=self.username,
                                         password=self.password,
                                         port=self.port,
                                         dbname=self.dbname)
        except psycopg2.DatabaseError as e:
            logging.error(e)
            sys.exit()
        finally:
            logging.info('Connection opened successfully.')

    def select_rows(self, query):
        """Run a SQL query to select rows from table."""
        if self.conn is None:
            self.open_connection()
        with self.conn.cursor() as cur:
            records = []
            cur.execute(query)
            result = cur.fetchall()
            for row in result:
                records.append(row)
            cur.close()
            return records

    def update_rows(self, query):
        """Run a SQL query to update rows in table."""
        if self.conn is None:
            self.open_connection()
        with self.conn.cursor() as cur:
            cur.execute(query)
            self.conn.commit()
            cur.close()
            return f"{cur.rowcount} rows affected."
