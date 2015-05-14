__author__ = 'Andre'

from tkinter import messagebox
from tkinter import *
import sqlite3
from ClassManager import cxn, cur

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
        self.txtBoxEmployeeFirstName = Entry(self.master, textvariable=self.firstName)
        self.lblLast = Label(self.master, text="Last Name: ")
        self.txtBoxEmployeeLastName = Entry(self.master, textvariable=self.lastName)
        self.lblAddress = Label(self.master, text="Address: ")
        self.txtBoxEmployeeAddress = Entry(self.master, textvariable=self.address)
        self.lblAmountDue = Label(self.master, text="Amount Due: ")
        self.txtBoxAmountDue = Entry(self.master, textvariable=self.amountDue)

        #Close Button
        self.btnClose = Button(self.master, text="Close", width=8, command=self.quit)

        #Aligns button in grid
        self.btnClose.grid(row=6, column=2)

        #Aligns the labels using the grid
        self.lblFirst.grid(row=1, column=1, sticky=W)
        self.txtBoxEmployeeFirstName.grid(row=1, column=2, sticky=E)
        self.lblLast.grid(row=2, column=1, sticky=W)
        self.txtBoxEmployeeLastName.grid(row=2, column=2)
        self.lblAddress.grid(row=3, column=1, sticky=W)
        self.txtBoxEmployeeAddress.grid(row=3, column=2)
        self.lblAmountDue.grid(row=4, column=1, sticky=W)
        self.txtBoxAmountDue.grid(row=4, column=2)
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

        if first == '' or last == '' or address == '':
            messagebox.showwarning("Error", "Please fill in all empty text boxes!")
            # set focus back to window
            self.master.focus_force()

        if amountDue < 0:
            messagebox.showwarning("Warning", "Please enter a positive number into the Amount Due field.")

            # set focus back to window and delete textbox contents
            self.master.focus_force()
            self.txtBoxAmountDue.delete(0, 'end')

        else:
            try:
                cur.execute('INSERT INTO Student VALUES(NULL, ?, ?, ?, ?)', (first, last, address, amountDue,))
                messagebox.showwarning("New Student Added", "New Student successfully added")

                # clear textboxes after successfully adding
                self.txtBoxEmployeeLastName.delete(0, 'end')
                self.txtBoxEmployeeFirstName.delete(0, 'end')
                self.txtBoxEmployeeAddress.delete(0, 'end')
                self.txtBoxAmountDue.delete(0, 'end')

            except sqlite3.IntegrityError:
                messagebox.showwarning("Error", "New Student could not be added")
                # set focus back to window
                self.master.focus_force()

            except ValueError:
                messagebox.showwarning("Warning", "Please enter a number in the amount due text field")

                # set focus back to window and delete textbox contents
                self.master.focus_force()
                self.txtBoxAmountDue.delete(0, 'end')

            finally:
                cxn.commit()

