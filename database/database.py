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


def get_results(query, need=False):
    """Set up database connection, execute query and close all"""
    rows = None
    user = config.identify()
    connect_str = "dbname='{}' user='{}' host='localhost' password='{}'".format(user[0], user[1], user[2])
    connection = psycopg2.connect(connect_str)
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute(query)
    if need:
        rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows

if __name__ == '__main__':
    pass
