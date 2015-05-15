__author__ = 'Andre'

from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import sqlite3
from ClassManager import cur, cxn


class AddStudentCourse:
    # Class for deleting Instructors
    # myMainWindowClass = MainWindow(empName)
    def __init__(self, master):

        # creates master window for calculation window, changes title, and sets size
        self.master = master
        self.master.title("Register Student")
        self.master.geometry("220x70")

        self.courseValues = []
        self.studentValues = []
        self.studentID = {}
        self.courseID = {}
        self.sequenceCount = 1

        # get the values from the database for the combo boxes
        try:
            cur.execute("SELECT description, code FROM Class")
            for course in cur.fetchall():
                # have to parse into string and access placeholder here because fetch... returns tuple
                stringCourse = str(course[0])
                self.courseValues.append(stringCourse)
                self.courseID[stringCourse] = course[1]

            cur.execute("SELECT firstName, lastName, id  FROM Student")
            for student in cur.fetchall():
                # have to parse into string and access placeholder here because fetch... returns tuple
                stringCourse = str(student[0]) + " " + str(student[1])
                self.studentValues.append(stringCourse)
                self.studentID[stringCourse] = student[2]
        except sqlite3.Connection:
            messagebox.showerror("Could not connect to the database")

        # create a combobox to store in the courses
        # https://docs.python.org/3.1/library/tkinter.ttk.html#combobox
        self.courseCombo = ttk.Combobox(self.master, values=self.courseValues, state="readonly")
        # set the current selection to the first item
        self.courseCombo.current(0)
        self.courseCombo.grid(row=3, column=2)

        self.studentCombo = ttk.Combobox(self.master, values=self.studentValues, state="readonly")
        self.studentCombo.current(0)
        self.studentCombo.grid(row=1, column=2)

        # Creates labels for outputting the calculations
        self.lblStudent = Label(self.master, text="Student: ")

        # Close Button
        self.btnClose = Button(self.master, text="Close", width=8, command=self.quit)

        # Aligns button in grid
        self.btnClose.grid(row=2, column=2)

        # Aligns the labels using the grid
        self.lblStudent.grid(row=1, column=1, sticky=W)

        self.btnRegister = Button(self.master, text="Register", width=8, command=self.register)
        self.btnRegister.grid(row=2, column=1)

    def quit(self):
        self.master.destroy()

    def register(self):
        # get the current combobox values
        student = self.studentCombo.get()
        course = self.courseCombo.get()
        courseID = self.courseID.get(course)
        studentid = self.studentID.get(student)
        # no need to validate because cannot be null and not different than
        # whats in the database
        # but need to figure out sequence
        try:
            # Validate student registration by checking if he is already registered for that class
            cur.execute('SELECT studentID  FROM ClassStudent WHERE studentID = ? AND code = ?', (studentid, courseID,))
            if cur.fetchone():
                messagebox.showwarning("Warning", "The student you selected is already registered for that class")
                # set focus back to window
                self.master.focus_force()
            else:
                cur.execute('SELECT COUNT(sequence) as num FROM ClassStudent WHERE studentID = ?', (studentid,))
                sequence = self.sequenceCount + cur.fetchone()[0]

                cur.execute('Insert INTO ClassStudent VALUES (?, ?, ?)', (courseID, sequence, studentid))
                messagebox.showwarning("Class Registered", " Class successfully registered")
                self.master.focus_force()

        except sqlite3.Error as e:
            messagebox.showwarning(e)

        finally:
            cxn.commit()