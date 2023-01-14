import psycopg2

def IniciarPsycopg():
    conn = psycopg2.connect(
        database="Escola",
        user='postgres',
        password='postgres',
        host='localhost',
        port='5432'
        )
        
    conn.autocommit = True

    cursor = conn.cursor()
    
    return cursor, conn


CURSOR,CONN = IniciarPsycopg()
