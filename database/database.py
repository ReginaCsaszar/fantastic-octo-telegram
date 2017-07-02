"""Function to use the database

users (
    id serial NOT NULL,
    username varchar UNIQUE,
    password varchar
    );

planet_votes (
    id serial NOT NULL,
    planet_id integer,
    planet_name varchar,
    users_id integer,
    submission_time char(16)
);
"""
import psycopg2
from database import config

import os
import urllib


def get_results(query, need=False):
    rows = None
    urllib.parse.uses_netloc.append('postgres')
    url = urllib.parse.urlparse(os.environ.get('DATABASE_URL'))
    connection = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute(query)
    if need:
        rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows

"""
    user = config.identify()
    connection = psycopg2.connect(
        dbname=user[0],
        user=user[1],
        password=user[2],
        host='localhost',
    )
"""
