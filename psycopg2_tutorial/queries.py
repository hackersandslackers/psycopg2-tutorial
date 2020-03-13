"""Read .sql files from a local folder."""
from os import listdir
from os.path import isfile, join


def get_sql_files(folder):
    """Fetch all SQL query files in folder."""
    files = [folder + '/' + f for f in listdir(folder) if isfile(join(folder, f)) if '.sql' in f]
    return files


def read_sql_from_files(folder):
    """Read SQL query from .sql file."""
    files = get_sql_files(folder)
    queries = []
    for file in files:
        fd = open(file, 'r')
        query = fd.read()
        queries.append(query)
        fd.close()
    return queries
