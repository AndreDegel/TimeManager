__author__ = 'Andre'

from tkinter import messagebox
from tkinter import *
import sqlite3
from ClassManager import cxn, cur


#Class for deleting Instructors
class DeleteInstructor:

    #myMainWindowClass = MainWindow(empName)
    def __init__(self, master):

        #creates master window for calculation window, changes title, and sets size
        self.master = master
        self.master.title("Delete Instructor")
        self.master.geometry("220x70")

        self.lastName = StringVar()

        #Creates labels for outputting the calculations
        self.lblLast = Label(self.master, text="Last Name: ")
        self.txtBoxEmployeeLastName = Entry(self.master, textvariable=self.lastName)


        #Close Button
        self.btnClose = Button(self.master, text="Close", width=8, command=self.quit)

        #Aligns button in grid
        self.btnClose.grid(row=2, column=2)

        #Aligns the labels using the grid
        self.lblLast.grid(row=1, column=1, sticky=W)
        self.txtBoxEmployeeLastName.grid(row=1, column=2)

        self.btnDelete = Button(self.master, text="Delete", width=8, command=self.delete)
        self.btnDelete.grid(row=2, column=1)

    def quit(self):
        self.master.destroy()

    def delete(self):
        # Delete instructors to the database
        last = self.lastName.get()

        if last == '':
            messagebox.showwarning("Error", "Please specify the instructor you want to delete!")
            self.master.focus_force()

        else:
            try:
                cur.execute('DELETE FROM Instructor WHERE lastName = ?', (last,))
                messagebox.showwarning("Instructor Deleted", " Instructor successfully deleted")
                # set focus back to window and delete textbox entry
                self.master.focus_force()
                self.txtBoxEmployeeLastName.delete(0, 'end')


            except sqlite3.Error as e:
                messagebox.showwarning(e)

            finally:
                cxn.commit()
