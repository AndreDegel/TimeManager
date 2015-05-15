__author__ = 'Andre'

from tkinter import messagebox, ttk
from tkinter import *
import sqlite3
from ClassManager import cur, cxn


# Class for searching for instructors, times, or classes
class Search:

    # myMainWindowClass = MainWindow(empName)
    def __init__(self, master):
        # creates master window for calculation window, changes title, and sets size
        self.master = master
        self.master.title("Search")
        self.master.geometry("300x300")

        # Sets the string variable and checkBox variables
        self.userSearchInput = StringVar()
        self.rdoVar = IntVar()

        # make a list of tuples for the radio buttons to configure
        searches = [("Search Instructor by Last Name", 1), ("Get Instructor Schedule by Last Name", 2),
                    ("Search Student by Last Name", 3), ("Search Class by Name", 4),
                    ("Search Class by Day", 5), ("Search Registered Students by Class", 6),
                    ("Retrieve Students time schedule", 7)]

        # Widgets
        self.lblSearchInformation = Label(self.master, text="Search For Instructor, Classes, or schedules")
        self.lblSearch = Label(self.master, text="Search: ")
        self.txtBoxSearch = Entry(self.master, textvariable=self.userSearchInput)
        self.combo = ttk.Combobox(self.master, state="readonly")

        # set up the radio buttons and position them on the grid
        for txt, val in searches:
            Radiobutton(self.master,
                        text=txt,
                        variable=self.rdoVar,
                        value=val,
                        justify=LEFT,
                        command=self.showText).grid(row=1+val, columnspan=1, sticky=W, )

        # Search Button
        self.btnSearch = Button(self.master, text="Search", width=12, command=self.searchQuery)
        # Close Button
        self.btnClose = Button(self.master, text="Close", width=12, command=self.quit)

        # Aligns the labels using the grid
        self.lblSearchInformation.grid(row=1, columnspan=1, sticky=W)
        self.lblSearch.grid(row=9, columnspan=1, sticky=W)

        self.btnSearch.grid(row=11, columnspan=1, sticky=W)
        self.btnClose.grid(row=12, columnspan=1, sticky=W)

    def showText(self):
        self.courseValues = []
        if self.rdoVar.get() == 4:
            self.getClassCodes()
            self.setCombo()
        elif self.rdoVar.get() == 5:
            self.getDays()
            self.setCombo()
        else:
            self.combo.grid_forget()
            self.txtBoxSearch.grid(row=10, columnspan=1, sticky=W)

    def getClassCodes(self):
        # configure values for course combo box with class codes
        try:
            cur.execute("SELECT description, code FROM Class")
            for course in cur.fetchall():
                # have to parse into string and access placeholder here because fetch... returns tuple
                stringCourse = str(course[0])
                self.courseValues.append(stringCourse)
        except sqlite3.Connection:
            messagebox.showerror("Could not connect to the database")

    def getDays(self):
        # configure values for course combo box with days
        try:
            cur.execute("SELECT DISTINCT Day FROM Schedule")
            for course in cur.fetchall():
                # have to parse into string and access placeholder here because fetch... returns tuple
                stringDay = str(course[0])
                self.courseValues.append(stringDay)
        except sqlite3.Connection:
            messagebox.showerror("Could not connect to the database")

    def setCombo(self):
        self.txtBoxSearch.grid_forget()
        self.combo.config(values=self.courseValues)
        self.combo.current(0)
        self.combo.grid(row=10, columnspan=1, sticky=W)

    # Searh Query Function
    def searchQuery(self):
        self.userSearchCriteria = self.userSearchInput.get()

        if self.userSearchCriteria == "" and self.rdoVar.get() != 4 and self.rdoVar.get() != 5:
            messagebox.showerror("Entry Error", "Textbox cannot be empty")
        else:
            try:
                # Gets the state of the checkboxes and then searches with the user input
                # it also accepts partial searches, so searching for "smith" or 's' will both return smith
                # Search Instructor by last name
                if self.rdoVar.get() == 1:
                    instructorlist = []
                    cur.execute("SELECT * FROM Instructor WHERE lastName LIKE ?", (self.userSearchCriteria + "%",))
                    for info in cur.fetchall():
                        instructor = "ID: " + str(info[0]) + " Name: " + info[1] + " " + info[2] + \
                                     " Address: " + info[3]
                        instructorlist.append(instructor)
                    msg = "\n".join(instructorlist)
                    messagebox.showinfo("Query Results", msg)

                # Get an instructors schedule by last name

                elif self.rdoVar.get() == 2:
                    instructorlist = []
                    cur.execute("SELECT firstName, lastName, description, Day, time  FROM Instructor, Class, Schedule "
                                "WHERE lastName LIKE ? AND Instructor.id = Class.instructorID "
                                "AND Class.code = Schedule.code", (self.userSearchCriteria,))
                    for info in cur.fetchall():
                        schedule = "Instructor" + info[0] + " " + info[1] + "Course: " + str(info[2]) + " Day: " \
                                   + info[3] + " Time: " + info[4] + "\n"
                        instructorlist.append(schedule)
                    msg = "\n".join(instructorlist)
                    messagebox.showinfo("Schedule", msg)

                # Search Student by last Name
                elif self.rdoVar.get() == 3:
                    studentList = []
                    cur.execute("SELECT * FROM Student WHERE lastName LIKE ?", (self.userSearchCriteria + "%",))
                    for info in cur.fetchall():
                        student = "ID: " + str(info[0]) + " Name: " + info[1] + " " + info[2] + " Address: " + info[3] + \
                                  " Amount Due: " + str(info[4])
                        studentList.append(student)
                    msg = "\n".join(studentList)
                    messagebox.showinfo("Query Results", msg)

                # Search Classes by class code
                elif self.rdoVar.get() == 4:
                    classlist = []
                    cur.execute("SELECT code, description, price, firstName, lastName FROM Class, Instructor "
                                "WHERE Class.instructorID = Instructor.id "
                                "AND description LIKE ?", (self.combo.get(),))
                    for info in cur.fetchall():
                        classes = "Code: " + str(info[0]) + " Description: " + info[1] + " Price: " + \
                                  str(info[2]) + " Instructor: " + \
                                  info[3] + " " + info[4]
                        classlist.append(classes)
                    msg = "\n".join(classlist)
                    messagebox.showinfo("Query Results", msg)

                # Search Schedule by day
                elif self.rdoVar.get() == 5:
                    scheduleList = []
                    cur.execute("SELECT description, Day, time FROM Schedule, Class WHERE Day LIKE ?",
                                (self.combo.get(),))
                    for info in cur.fetchall():
                        schedule = "Class: " + str(info[0]) + " Day: " + info[1] + " Time: " + info[2] + "\n"
                        scheduleList.append(schedule)
                    msg = "\n".join(scheduleList)
                    messagebox.showinfo("Query Results", msg)

                # Retrieve all registered students for a specific course
                elif self.rdoVar.get() == 6:
                    register = []
                    cur.execute("SELECT firstName, lastName, description FROM ClassStudent, Student, Class "
                                "WHERE ClassStudent.code = Class.code AND ClassStudent.studentID = Student.id "
                                "AND description LIKE ?", (self.userSearchCriteria + "%",))
                    for info in cur.fetchall():
                        registered = "Student: " + str(info[0]) + " " + str(info[1]) + " Registered for: " \
                                     + str(info[2]) + "\n"
                        register.append(registered)
                    msg = "\n".join(register)
                    messagebox.showinfo("Query Results", msg)

                # Get a students schedule by  his last name
                # Search by initial is disabled because query is too complex to search by initial
                elif self.rdoVar.get() == 7:
                    studentSchedule = []
                    cur.execute("SELECT Student.firstName, Student.lastName, description, Day, time, "
                                "Instructor.firstName, Instructor.lastName "
                                "FROM ClassStudent, Class, Schedule, Student, Instructor "
                                "WHERE Instructor.id = Class.instructorID AND Student.id = ClassStudent.studentID "
                                "AND Class.code = ClassStudent.code AND Class.code = Schedule.code "
                                "AND Student.lastName = ?", (self.userSearchCriteria,))
                    for info in cur.fetchall():
                        courseTimes = "Student: " + str(info[0]) + " " + str(info[1]) + "Course: " + str(info[2]) \
                                      + " Day: " + str(info[3]) + " Time:" + str(info[4]) + \
                                      " Instructor: " + str(info[5]) + " " + str(info[6] + "\n")
                        studentSchedule.append(courseTimes)
                    msg = "\n".join(studentSchedule)
                    messagebox.showinfo("Query Results", msg)

                # set focus back to window and clear the textbox after the search
                self.master.focus_force()
                self.txtBoxSearch.delete(0, 'end')

            except sqlite3.IntegrityError:
                messagebox.showwarning("Search Error", "No matches could be found")

            finally:

                cxn.commit()

    def quit(self):
        self.master.destroy()
