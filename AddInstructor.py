__author__ = 'Andre'

from tkinter import messagebox
from tkinter import *
import sqlite3
import ClassManager

#Class for displaying paycheck after calculations
class AddInstructor:

    #myMainWindowClass = MainWindow(empName)
    def __init__(self, master):

        #creates master window for calculation window, changes title, and sets size
        self.master = master
        self.master.title("Add Instructor")
        self.master.geometry("250x140")

        self.firstName = StringVar()
        self.lastName = StringVar()
        self.address = StringVar()

        #Creates labels for outputting the calculations
        self.lblFirst = Label(self.master, text="First Name: ")
        txtBoxEmployeeFirstName = Entry(self.master, textvariable=self.firstName)
        self.lblLast = Label(self.master, text="Last Name: ")
        txtBoxEmployeeLastName = Entry(self.master, textvariable=self.lastName)
        self.lblAddress = Label(self.master, text="Address: ")
        txtBoxEmployeeAddress = Entry(self.master, textvariable=self.address)

        #Close Button
        self.btnClose = Button(self.master, text="Close", width=8, command=self.quit)

        #Aligns button in grid
        self.btnClose.grid(row=5, column=2)

        #Aligns the labels using the grid
        self.lblFirst.grid(row=1, column=1, sticky=W)
        txtBoxEmployeeFirstName.grid(row=1, column=2, sticky=E)
        self.lblLast.grid(row=2, column=1, sticky=W)
        txtBoxEmployeeLastName.grid(row=2, column=2)
        self.lblAddress.grid(row=3, column=1, sticky=W)
        txtBoxEmployeeAddress.grid(row=3, column=2)
        self.btnAdd = Button(self.master, text="Add", width=8, command=self.add)
        self.btnAdd.grid(row=4, column=2)

    def quit(self):
        self.master.destroy()

    def add(self):
        # Add instructors to the database
        first = self.firstName.get()
        last = self.lastName.get()
        address = self.address.get()

        if first == '' or last == '' or address == '':
            messagebox.showwarning("Error", "Please fill in all empty text boxes!")

        else:
            try:
                cur.execute('INSERT INTO Instructor VALUES(NULL, ?, ?, ?)', (first, last, address,))
                messagebox.showwarning("New Instructor Added", "New Instructor successfully added")

            except sqlite3.IntegrityError:
                messagebox.showwarning("New Instructor could not be added")

            finally:
                ClassManager.cxn.commit()