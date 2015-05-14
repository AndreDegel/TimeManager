__author__ = 'Andre'

from tkinter import messagebox
from tkinter import *
import sqlite3
from ClassManager import cur, cxn

#TODO: Have students for classes by day/not all days.

#Class for searching for instructors, times, or classes
class Search:

    #myMainWindowClass = MainWindow(empName)
    def __init__(self, master):
        #creates master window for calculation window, changes title, and sets size
        self.master = master
        self.master.title("Search")
        self.master.geometry("300x280")

        #Sets the string variable and checkBox variables
        self.userSearchInput = StringVar()
        self.rdoVar = IntVar()
        searches = [("Search Instructor by Last Name", 1),
                    ("Search Student by Last Name", 2), ("Search Class by Name", 3),
                    ("Search Class by Day", 4), ("Search Registered Students by Class", 5),
                    ("Retrieve Students time schedule", 6)]

        # set up the radio buttons and position them on the grid
        for txt, val in searches:
            Radiobutton(self.master,
                        text=txt,
                        variable=self.rdoVar,
                        value=val,
                        justify=LEFT).grid(row=1+val, columnspan=1, sticky=W)



        #Widgets
        self.lblSearchInformation = Label(self.master, text="Search For Instructor, Classes, or schedules")
        self.lblSearch = Label(self.master, text="Search: ")
        self.txtBoxSearch = Entry(self.master, textvariable=self.userSearchInput)

        #Search Button
        self.btnSearch = Button(self.master, text="Search", width=12, command=self.searchQuery)
        #Close Button
        self.btnClose = Button(self.master, text="Close", width=12, command=self.quit)

        #Aligns the labels using the grid
        self.lblSearchInformation.grid(row=1, columnspan=1, sticky=W)
        self.lblSearch.grid(row=8, columnspan=1, sticky=W)
        self.txtBoxSearch.grid(row=9, columnspan=1, sticky=W)
        self.btnSearch.grid(row=10, columnspan=1, sticky=W)
        self.btnClose.grid(row=11, columnspan=1, sticky=W)

    #Searh Query Function
    def searchQuery(self):
        self.userSearchCriteria = self.userSearchInput.get()

        if(self.userSearchCriteria == ""):
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
                        instructor = "ID: " + str(info[0]) + " Name: " + info[1] + " " + info[2] + " Address: " + info[3]
                        instructorlist.append(instructor)
                    msg = "\n".join(instructorlist)
                    messagebox._show("Query Results", msg)

                #Search Student by last Name
                elif self.rdoVar.get() == 2:
                    studentList = []
                    cur.execute("SELECT * FROM Student WHERE lastName LIKE ?", (self.userSearchCriteria + "%",))
                    for info in cur.fetchall():
                        student = "ID: " + str(info[0]) + " Name: " + info[1] + " " + info[2] + " Address: " + info[3] + \
                                  " Amount Due: " + str(info[4])
                        studentList.append(student)
                    msg = "\n".join(studentList)
                    messagebox._show("Query Results", msg)

                # Search Classes by class code
                # TODO: my choose classes from drop down or by name
                elif self.rdoVar.get() == 3:
                    classlist = []
                    cur.execute("SELECT code, description, price, firstName, lastName FROM Class, Instructor WHERE Class.instructorID = Instructor.id "
                                "AND code LIKE ?", (self.userSearchCriteria + "%",))
                    for info in cur.fetchall():
                        classes = "Code: " + str(info[0]) + " Description: " + info[1] + " Price: " + str(info[2]) + " Instructor: " + \
                                  info[3] + " " + info[4]
                        classlist.append(classes)
                    msg = "\n".join(classlist)
                    messagebox._show("Query Results", msg)

                # Search Schedule by day
                elif self.rdoVar.get() == 4:
                    scheduleList = []
                    cur.execute("SELECT * FROM Schedule WHERE Day LIKE ?", (self.userSearchCriteria + "%",))
                    for info in cur.fetchall():
                        schedule = "Code: " + str(info[0]) + " Day: " + info[1] + " Time: " + info[2]
                        scheduleList.append(schedule)
                    msg = "\n".join(scheduleList)
                    messagebox._show("Query Results", msg)

                # Retrieve all registered students for a specific course
                elif self.rdoVar.get() == 5:
                    register = []
                    cur.execute("SELECT firstName, lastName, description FROM ClassStudent, Student, Class "
                                "WHERE ClassStudent.code = Class.code AND ClassStudent.studentID = Student.id "
                                "AND description LIKE ?", (self.userSearchCriteria + "%",))
                    for info in cur.fetchall():
                        registered = "Student: " + str(info[0]) + str(info[1]) + " Registered for: " + str(info[2]) +"\n"
                        register.append(registered)
                    msg = "\n".join(register)
                    messagebox._show("Query Results", msg)

                # Get a students schedule by  his last name
                elif self.rdoVar.get() == 6:
                    studentSchedule = []
                    cur.execute("SELECT Student.firstName, Student.lastName, description, Day, time, "
                                "Instructor.firstName, Instructor.lastName "
                                "FROM ClassStudent, Class, Schedule, Student, Instructor "
                                "WHERE Instructor.id = Class.instructorID AND Student.id = ClassStudent.studentID "
                                "AND Class.code = ClassStudent.code AND Class.code = Schedule.code "
                                "AND Student.lastName = ?", (self.userSearchCriteria + "%",))
                    for info in cur.fetchall():
                        courseTimes = "Student: " + str(info[0]) + " " + str(info[1]) + "Course: " + str(info[2]) \
                                      + " Day: " + str(info[3]) + " Time:" + str(info[4]) +\
                                     " Instructor: " + str(info[5]) + " " + str(info[6] +"\n")
                        studentSchedule.append(courseTimes)
                    msg = "\n".join(studentSchedule)
                    messagebox._show("Query Results", msg)

                # set focus back to window and clear the textbox after the search
                self.master.focus_force()
                self.txtBoxSearch.delete(0, 'end')

            except sqlite3.IntegrityError:
                messagebox.showwarning("Search Error", "No matches could be found")

            finally:

                cxn.commit()

    def quit(self):
        self.master.destroy()
