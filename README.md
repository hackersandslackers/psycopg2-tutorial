# Psycopg2 Tutorial

![Python](https://img.shields.io/badge/Python-v3.8-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
![Psycopg2-Binary](https://img.shields.io/badge/Psycopg2--binary-v2.8.4-blue.svg?longCache=true&logo=postgresql&longCache=true&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![GitHub Last Commit](https://img.shields.io/github/last-commit/google/skia.svg?style=flat-square&colorA=4c566a&colorB=a3be8c)
[![GitHub Issues](https://img.shields.io/github/issues/hackersandslackers/psycopg2-tutorial.svg?style=flat-square&colorA=4c566a&colorB=ebcb8b&logo=Github)](https://github.com/hackersandslackers/psycopg2-tutorial/issues)
[![GitHub Stars](https://img.shields.io/github/stars/hackersandslackers/psycopg2-tutorial.svg?style=flat-square&colorA=4c566a&colorB=ebcb8b&logo=Github)](https://github.com/hackersandslackers/psycopg2-tutorial/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/hackersandslackers/psycopg2-tutorial.svg?style=flat-square&colorA=4c566a&colorB=ebcb8b&logo=Github)](https://github.com/hackersandslackers/psycopg2-tutorial/network)

![Psycopg2-Tutorial](https://github.com/hackersandslackers/psycopg2-tutorial/blob/master/.github/psycopg2@2x.jpg?raw=true)

Source code for the accompanying tutorial found here: https://hackersandslackers.com/psycopg2-postgres-python/

Connect to a PostgreSQL database and execute queries in Python using the Psycopg2 library using this tutorial. This script looks for **.sql** files stored in the **/queries** directory, and executes them against a Postgres database.


## Getting Started

**Installation via `requirements.txt`**:

```shell
$ git clone https://github.com/hackersandslackers/psycopg2-tutorial.git
$ cd psycopg2-tutorial
$ python3 -m venv myenv
$ source myenv/bin/activate
$ pip3 install -r requirements.txt
$ python3 main.py
```

**Installation via [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/)**:

```shell
$ git clone https://github.com/hackersandslackers/psycopg2-tutorial.git
$ cd psycopg2-tutorial
$ pipenv shell
$ pipenv update
$ python3 main.py
```

**Installation via [Poetry](https://python-poetry.org/)**:

```shell
$ git clone https://github.com/hackersandslackers/psycopg2-tutorial.git
$ cd psycopg2-tutorial
$ poetry shell
$ poetry update
$ poetry run
```

## Usage

Replace the values in **.env.example** with your values and rename this file to **.env**:

* `DATABASE_USERNAME`: The username used to connect to your Postgres database.
* `DATABASE_PASSWORD`: Password for the above user.
* `DATABASE_HOST`: The hostname of your database (ie: localhost).
* `DATABASE_NAME`: The name of your "database" (the database inside your database - why isn't there a better term for this?).
* `DATABASE_PORT`: Port of your Postgres database (default is 5432).

*Remember never to commit secrets saved in .env files to Github.*

-----

**Hackers and Slackers** tutorials are free of charge. If you found this tutorial helpful, a [small donation](https://www.buymeacoffee.com/hackersslackers) would be greatly appreciated to keep us in business. All proceeds go towards coffee, and all coffee goes towards more content.
