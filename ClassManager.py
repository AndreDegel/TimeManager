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
    # create the table and fill it with data
'''
cur.execute('CREATE TABLE Instructor(id INTEGER PRIMARY KEY, firstName VARCHAR(50), lastName VARCHAR(50), address VARCHAR(50))')
cur.execute('CREATE TABLE Class(code VARCHAR(8) PRIMARY KEY, description VARCHAR(50), price FLOAT, instructorID INTEGER REFERENCES Instructor(id))')
cur.execute('CREATE TABLE Schedule(code VARCHAR(8) REFERENCES Class(code), Day TEXT, time TEXT)')
cur.execute('CREATE TABLE Student(id INTEGER PRIMARY KEY, firstName VARCHAR(50), lastName VARCHAR(50), address VARCHAR(50), amountDue FLOAT)')
cur.execute('CREATE TABLE ClassStudent(code VARCHAR(8) REFERENCES Class(code), sequence INTEGER, studentID INTEGER REFERENCES Student(id))')
'''

cur.execute('INSERT INTO Instructor VALUES(NULL, "Bob", "Smith", "1234 Street")')
cur.execute('INSERT INTO Class VALUES("Weight", "Lifting weights", 250.00, 1)')
cur.execute('INSERT INTO Schedule VALUES("Weight", "Monday", "19:00")')
cur.execute('INSERT INTO ClassStudent VALUES("Weight", 1, 1)')
cur.execute('INSERT INTO Student VALUES(1, "Jane", "Smith", "1500 Tree Rd.", 0)')
'''
cur.execute('SELECT * FROM Instructor')
cur.execute('SELECT * FROM Class')
cur.execute('SELECT * FROM Schedule')
cur.execute('SELECT * FROM ClassStudent')
cur.execute('SELECT * FROM Student')'''
# handle an sql exception if the table already exists