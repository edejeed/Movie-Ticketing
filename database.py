import sqlite3

conn = sqlite3.connect('MovieTicketingSystem.db')
cur = conn.cursor()


def create_table(sql_statement=None):
    try:
        cur.execute(sql_statement)
    except:
        print('Cannot create table.')



# main
from ddl import tables
for i in tables:
    create_table(i)