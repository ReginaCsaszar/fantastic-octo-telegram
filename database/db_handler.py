"""Function to use the database"""
import psycopg2
from database import config


def get_results(query):
    """Set up database connection, execute query and close all"""
    user = identify()
    connect_str = "dbname='{}' user='{}' host='localhost' password='{}'".format(user[0], user[1], user[2])
    connection = psycopg2.connect(connect_str)
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()


if __name__ == '__main__':
    pass
