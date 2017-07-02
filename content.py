"""Content handler program functions"""
from database import database


def get_stats():
    data = database.get_results("""SELECT COUNT(*), planet_name
                                    FROM planet_votes
                                        GROUP BY planet_name
                                        ORDER BY count(*) DESC;""", True)
    return data


if __name__ == '__main__':
    pass
