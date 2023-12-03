from sqlite3 import *

def first_connection():
    conn = connect('TicTacToe.db')
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS players(
            first_name text,
            score INTEGER DEFAULT NULL)
        """)
    conn.commit()
    conn.close()

def alter():
    conn = connect('TicTacToe.db')
    c = conn.cursor()

    c.execute("""ALTER TABLE players ADD score integer DEFAULT null""")
    conn.commit()
    conn.close()
    
def add(first):
    conn = connect('TicTacToe.db')
    c = conn.cursor()
    
    c.execute("""INSERT INTO players VALUES (?,?)""",(first,0))
    conn.commit()
    conn.close()
    
def drop():
    conn = connect('TicTacToe.db')
    c = conn.cursor()
    
    c.execute("""DROP TABLE IF EXISTS players""")
    conn.commit()
    conn.close()
    
def update1(score):
    conn = connect('TicTacToe.db')
    c = conn.cursor()
    
    c.execute("""UPDATE players SET
            score = (?) WHERE rowid = 1""",(score,))
    conn.commit()
    conn.close()
    
def update2(score):
    conn = connect('TicTacToe.db')
    c = conn.cursor()
    
    c.execute("""UPDATE players SET
            score = (?) WHERE rowid = 2""",(score,))
    conn.commit()
    conn.close()
    
def select():
    conn = connect('TicTacToe.db')
    c = conn.cursor()

    c.execute("""SELECT rowid, * FROM players WHERE rowid = 1""")
    result = c.fetchone()  
    conn.commit()
    conn.close()
    return result

def select1():
    conn = connect('TicTacToe.db')
    c = conn.cursor()

    c.execute("""SELECT rowid, * FROM players WHERE rowid = 2""")
    result = c.fetchone()  
    conn.commit()
    conn.close()
    return result