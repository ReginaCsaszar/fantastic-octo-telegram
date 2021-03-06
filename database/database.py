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

import os
import psycopg2
import urllib


def get_results(query, need=False):
    rows = None
    urllib.parse.uses_netloc.append('postgres')
    url = urllib.parse.urlparse(os.environ.get('DATABASE_URL'))
    try:
        connection = psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
            )
    except psycopg2.OperationalError:
        connection = psycopg2.connect(
            dbname='wosw',
            user='jeannie',
            password='57231024',
            host='localhost',
        )
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute(query)
    if need:
        rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows
