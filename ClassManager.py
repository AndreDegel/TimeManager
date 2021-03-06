__author__ = 'Andre'

from tkinter import *
import sqlite3
import MainMenu

'''
Gym classes time manager
'''

# not in class or function, to give access to the same connection over all other classes
# create a connection to the newly made database
cxn = sqlite3.connect('GymDB')
# initialize a cursor object to run execute commands on the connected database.
cur = cxn.cursor()


def createTables():
    # create the table and fill it with data
    # start a try-except block to handle SQL-Exceptions
    # pu in function in case it has to be recreated
    try:
        cur.execute('CREATE TABLE Instructor(id INTEGER PRIMARY KEY, firstName VARCHAR(50), lastName VARCHAR(50), address VARCHAR(50))')
        cur.execute('CREATE TABLE Class(code VARCHAR(8) PRIMARY KEY, description VARCHAR(50), price FLOAT, instructorID INTEGER REFERENCES Instructor(id))')
        cur.execute('CREATE TABLE Schedule(code VARCHAR(8) REFERENCES Class(code), Day TEXT, time TEXT)')
        cur.execute('CREATE TABLE Student(id INTEGER PRIMARY KEY, firstName VARCHAR(50), lastName VARCHAR(50), address VARCHAR(50), amountDue FLOAT)')
        cur.execute('CREATE TABLE ClassStudent(code VARCHAR(8) REFERENCES Class(code), sequence INTEGER, studentID INTEGER REFERENCES Student(id))')
    except sqlite3.OperationalError:
        print("The tables have been created already")

    # Create some test data
    # function to call if test data gets lost


def insert():
    try:
        cur.execute('INSERT INTO Instructor VALUES(NULL, "Bob", "Smith", "1234 Street")')
        cur.execute('INSERT INTO Class VALUES("Weight", "Lifting weights", 250.00, 1)')
        cur.execute('INSERT INTO Schedule VALUES("Weight", "Monday", "19:00")')
        cur.execute('INSERT INTO ClassStudent VALUES("Weight", 1, 1)')
        cur.execute('INSERT INTO Student VALUES(NULL, "Jane", "Smith", "1500 Tree Rd.", 0)')
    except sqlite3.IntegrityError:
        print("Test data has been put in already")


def drop():
    try:
        cur.execute('DROP TABLE Instructor')
        cur.execute('DROP TABLE Class')
        cur.execute('DROP TABLE Schedule')
        cur.execute('DROP TABLE ClassStudent')
        cur.execute('DROP TABLE Student')
    except sqlite3.Error:
        print("Test tables could not be dropped")


# Creates the root window and loops it
def main():
    root = Tk()
    MainMenu.MainWindow(root)
    root.mainloop()

# Loops the code so the windows stay open
if __name__ == "__main__":
    main()