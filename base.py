import sqlite3
from contextlib import contextmanager


def get_all_base() -> list:
    con = sqlite3.connect('data/coffee.sqlite')
    sql = con.cursor()
    result = sql.execute("""SELECT cof.id, v.title, d.title, c.title, cof.description, cof.price, cof.volume FROM 
    coffee cof, conditions c, degree_roasting d, varietys v 
    WHERE cof.variety = v.id AND cof.condition = c.id AND cof.degree_roasting = d.id""").fetchall()
    con.close()
    return result


def get_base_data(url: str, data: tuple or dict = None) -> list:
    data = tuple() if not data else data
    con = sqlite3.connect('data/coffee.sqlite')
    sql = con.cursor()
    result = sql.execute(url, data).fetchall()
    con.close()
    return result


@contextmanager
def get_base(path: str, is_commit: bool = False):
    try:
        con = sqlite3.connect(path)
        sql = con.cursor()
        yield sql
    finally:
        if is_commit:
            con.commit()
        con.close()
