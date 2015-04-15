__author__ = 'Andre'

import sqlite3
'''
Beginning example code for time manager
'''

# create a connection to the newly made database
cxn = sqlite3.connect('GymDB')
# initialize a cursor object to run execute commands on the connected database.
cur = cxn.cursor()
# start a try-except block to handle SQL-Exceptions
try:
    # create the table and fill it with data
    cur.execute('CREATE TABLE Students(login VARCHAR(8), userid INTEGER, salary FLOAT)')
    '''cur.execute('INSERT INTO users VALUES("John", 100, 1000.00)')
    cur.execute('INSERT INTO users VALUES("Jane", 110, 2500.00)')
    cur.execute('INSERT INTO users VALUES("Jim", 120, 1500.00)')
    cur.execute('INSERT INTO users VALUES("Bob", 130, 2000.00)')
    cur.execute('SELECT * FROM users')'''

# handle an sql exception if the table already exists
except sqlite3.OperationalError:
    print("The table exists already")