from connect_database import *

def filter_genre(value):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.data_games WHERE genre=$$%s$$" % (value))
    res = cursor.fetchall()
    for elem in res:
        print(elem)

def filter_year(value):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.data_games WHERE year=%s" % (value))
    res = cursor.fetchall()
    for elem in res:
        print(elem)

def filter_publisher(value):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.data_games WHERE publisher='%s'" % (value))
    res = cursor.fetchall()
    for elem in res:
        print(elem)

