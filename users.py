"""User handler program functions"""
from database import database


def register_new(user, psw):
    database.get_results("""INSERT INTO users (username, password) VALUES ('{0}', '{1}');""".format(user, psw))


def get_psw(user):
    psw = database.get_results("""SELECT password FROM users WHERE username='{0}';""".format(user), True)
    return psw[0][0]
