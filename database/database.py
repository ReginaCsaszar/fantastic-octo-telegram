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


def get_results(query, need=False):
    rows = None
    user = config.identify()
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
