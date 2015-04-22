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
try:
    cur.execute('CREATE TABLE Instructor(id INTEGER PRIMARY KEY, firstName VARCHAR(50), lastName VARCHAR(50), address VARCHAR(50))')
    cur.execute('CREATE TABLE Class(code VARCHAR(8) PRIMARY KEY, description VARCHAR(50), price FLOAT, instructorID INTEGER REFERENCES Instructor(id))')
    cur.execute('CREATE TABLE Schedule(code VARCHAR(8) REFERENCES Class(code), Day TEXT, time TEXT)')
    cur.execute('CREATE TABLE Student(id INTEGER PRIMARY KEY, firstName VARCHAR(50), lastName VARCHAR(50), address VARCHAR(50), amountDue FLOAT)')
    cur.execute('CREATE TABLE ClassStudent(code VARCHAR(8) REFERENCES Class(code), sequence INTEGER, studentID INTEGER REFERENCES Student(id))')
except sqlite3.OperationalError:
    print("The tables have been created already")

try:
    cur.execute('INSERT INTO Instructor VALUES(NULL, "Bob", "Smith", "1234 Street")')
    cur.execute('INSERT INTO Class VALUES("Weight", "Lifting weights", 250.00, 1)')
    cur.execute('INSERT INTO Schedule VALUES("Weight", "Monday", "19:00")')
    cur.execute('INSERT INTO ClassStudent VALUES("Weight", 1, 1)')
    cur.execute('INSERT INTO Student VALUES(NULL, "Jane", "Smith", "1500 Tree Rd.", 0)')
except sqlite3.IntegrityError:
    print("Test data has been put in already")

#  To retrieve data after executing a SELECT statement, you can either treat the cursor as an iterator,
#  call the cursor’s fetchone() method to retrieve a single matching row, or call fetchall() to get a list of the matching rows.
try:
    cur.execute('SELECT * FROM Instructor')
    for eachUser in cur.fetchall():
        print("Successfully created the users table.")
        print(eachUser)

    cur.execute('SELECT * FROM Class')
    for eachUser in cur.fetchall():
        print("Successfully created the users table.")
        print(eachUser)

    cur.execute('SELECT * FROM Schedule')
    for eachUser in cur.fetchall():
        print("Successfully created the users table.")
        print(eachUser)

    cur.execute('SELECT * FROM ClassStudent')
    for eachUser in cur.fetchall():
        print("Successfully created the users table.")
        print(eachUser)

    cur.execute('SELECT * FROM Student')
    for eachUser in cur.fetchall():
        print("Successfully created the users table.")
        print(eachUser)
    # handle an sql exception if the table already exists
except sqlite3.OperationalError:
    print("Could not retrieve data")

# Final block runs always so that if something went wrong we can at least close the connection and commit whatever went through
finally:
    cur.close()
    cxn.commit()
    cxn.close()