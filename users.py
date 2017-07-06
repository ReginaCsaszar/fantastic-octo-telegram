"""User handler program functions"""
from database import database


def register_new(user, psw):
    database.get_results("""INSERT INTO users (username, password) VALUES ('{0}', '{1}');""".format(user, psw))


def get_psw(user):
    psw = database.get_results("""SELECT password FROM users WHERE username='{0}';""".format(user), True)
    return psw[0][0]


def handle_vote(planet_name, planet_id, user):
    database.get_results("""INSERT INTO planet_votes (planet_id, planet_name, users_id)
                                VALUES ({0}, '{1}',(SELECT id
                                    FROM users WHERE username='{2}'));""".format(planet_id, planet_name, user))
