import psycopg2
from config import config

def connect():
    """ Connect to the PostgreSQL database """
    conn = None
    try:
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the db...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute('SELECT version()')
        print('PostgreSQL database version:')
        print(cur.fetchone()) # fetches db version
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()
