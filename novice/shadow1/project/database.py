import psycopg2


def kon():
    conn = psycopg2.connect(
        database='postgres', 
        user='john', 
        host='localhost',
        password='1234',)


    conn.autocommit = True
