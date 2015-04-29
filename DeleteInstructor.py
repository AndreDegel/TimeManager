__author__ = 'Andre'

from tkinter import messagebox
from tkinter import *
import sqlite3

# create a connection to the newly made database
cxn = sqlite3.connect('GymDB')
# initialize a cursor object to run execute commands on the connected database.
cur = cxn.cursor()

#Class for deleting Instructors
class DeleteInstructor:

    #myMainWindowClass = MainWindow(empName)
    def __init__(self, master):

        #creates master window for calculation window, changes title, and sets size
        self.master = master
        self.master.title("Delete Instructor")
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
        self.btnDelete = Button(self.master, text="Delete", width=8, command=self.delete)
        self.btnDelete.grid(row=4, column=2)

    def quit(self):
        self.master.destroy()

    def delete(self):
        # Delete instructors to the database
        first = self.firstName.get()
        last = self.lastName.get()
        address = self.address.get()
        try:
            cur.execute('DELETE FROM Instructor')
            messagebox.showwarning("Instructor Deleted", " Instructor successfully deleted")

        except sqlite3.IntegrityError:
            messagebox.showwarning("Instructor could not be deleted")

        finally:
            #cur.close()
            cxn.commit()
            #cxn.close()
