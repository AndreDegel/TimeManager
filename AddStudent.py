__author__ = 'Andre'

from tkinter import messagebox
from tkinter import *
import sqlite3

# create a connection to the newly made database
cxn = sqlite3.connect('GymDB')
# initialize a cursor object to run execute commands on the connected database.
cur = cxn.cursor()

#Class for adding students to the database
class AddStudent:

    def __init__(self, master):

        #creates master window for calculation window, changes title, and sets size
        self.master = master
        self.master.title("Add Student")
        self.master.geometry("250x140")

        self.firstName = StringVar()
        self.lastName = StringVar()
        self.address = StringVar()
        self.amountDue = DoubleVar()

        #Creates labels for outputting the calculations
        self.lblFirst = Label(self.master, text="First Name: ")
        txtBoxEmployeeFirstName = Entry(self.master, textvariable=self.firstName)
        self.lblLast = Label(self.master, text="Last Name: ")
        txtBoxEmployeeLastName = Entry(self.master, textvariable=self.lastName)
        self.lblAddress = Label(self.master, text="Address: ")
        txtBoxEmployeeAddress = Entry(self.master, textvariable=self.address)
        self.lblAmountDue = Label(self.master, text="Amount Due: ")
        txtBoxAmountDue = Entry(self.master, textvariable=self.amountDue)

        #Close Button
        self.btnClose = Button(self.master, text="Close", width=8, command=self.quit)

        #Aligns button in grid
        self.btnClose.grid(row=6, column=2)

        #Aligns the labels using the grid
        self.lblFirst.grid(row=1, column=1, sticky=W)
        txtBoxEmployeeFirstName.grid(row=1, column=2, sticky=E)
        self.lblLast.grid(row=2, column=1, sticky=W)
        txtBoxEmployeeLastName.grid(row=2, column=2)
        self.lblAddress.grid(row=3, column=1, sticky=W)
        txtBoxEmployeeAddress.grid(row=3, column=2)
        self.lblAmountDue.grid(row=4, column=1, sticky=W)
        txtBoxAmountDue.grid(row=4, column=2)
        self.btnAdd = Button(self.master, text="Add", width=8, command=self.add)
        self.btnAdd.grid(row=5, column=2)

    def quit(self):
        self.master.destroy()

    def add(self):
        # Add student to the database
        first = self.firstName.get()
        last = self.lastName.get()
        address = self.address.get()
        amountDue = self.amountDue.get()

        try:
            cur.execute('INSERT INTO Student VALUES(NULL, ?, ?, ?, ?)', (first, last, address, amountDue,))
            messagebox.showwarning("New Student Added", "New Student successfully added")

            cur.execute('SELECT * FROM Student')
            for eachUser in cur.fetchall():
                print("Successfully created the users table.")
                print(eachUser)

        except sqlite3.IntegrityError:
            messagebox.showwarning("New Student could not be added")

        finally:
            #cur.close()
            cxn.commit()
            #cxn.close()
