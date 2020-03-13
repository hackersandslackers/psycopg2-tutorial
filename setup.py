"""A setuptools based setup module."""
from os import path
from setuptools import setup, find_packages
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Psycopg2 Tutorial',
    version='0.1.0',
    description='Connect to a PostgreSQL database and execute queries in \
                 Python using the Psycopg2 library using this tutorial. This \
                 script looks for **.sql** files stored in the **/queries** \
                 directory and executes them against a Postgres database.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hackersandslackers/psycopg2-tutorial/',
    author='Todd Birchard',
    author_email='toddbirchard@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='Postgres PostgreSQL Psycopg2 Database Python',
    packages=find_packages(),
    install_requires=['psycopg2-binary',
                      'python-dotenv',
                      'loguru'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
        'env': ['python-dotenv']
    },
    entry_points={
        'console_scripts': [
            'run=main:__main__',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/hackersandslackers/psycopg2-tutorial/issues',
        'Source': 'https://github.com/hackersandslackers/psycopg2-tutorial/',
    },
)
