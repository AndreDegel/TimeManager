import ClassManager

__author__ = 'Andre'

from tkinter import *
from AddInstructor import AddInstructor
from AddStudent import AddStudent
from DeleteInstructor import DeleteInstructor
from AddStudentCourse import AddStudentCourse
from Search import Search

#Class for the Main Window
class MainWindow():

    def __init__(self, master):

            #sets window to master, sets title, and window size
            self.master = master
            self.master.title("Class Manager")
            self.master.geometry("300x200")

            #Declares and defines labels, buttons, and textboxes
            self.btnAddInstructor = Button(self.master, text="Add Instructor", width=17, command=self.addInstructor)
            self.btnAddStudent = Button(self.master, text="Add Student", width=17, command=self.addStudent)
            self.btnDeleteInstructor = Button(self.master, text="Delete Instructor", width=17, command=self.deleteInstructor)
            self.btnAddStudentCourse = Button(self.master, text="Add Student to Course", width=17, command=self.addStudentCourse)
            self.btnSearch = Button(self.master, text="Search", width=17, command=self.search)
            self.btnQuit = Button(self.master, text="Quit", width=17, command=self.quit)

            #Aligns all of the labels, buttons, and textboxes in grid form
            self.btnAddInstructor.grid(row=1, column=1, sticky=W)
            self.btnAddStudent.grid(row=2, column=1, sticky=W)
            self.btnDeleteInstructor.grid(row=3, column=1, sticky=W)
            self.btnAddStudentCourse.grid(row=4, column=1, sticky=W)
            self.btnSearch.grid(row=5, column=1, sticky=W)
            self.btnQuit.grid(row=6, column=1)

    #Function for quit button to close window
    def quit(self):
        ClassManager.cur.close()
        ClassManager.cxn.commit()
        ClassManager.cxn.close()
        self.master.destroy()

    #Function for displaying the add instructor window
    def addInstructor(self):
        #Sets the addInstructor class to root2 so it is displayed when Add Instructor button is clicked
        root2 = Toplevel(self.master)
        AddInstructor(root2)

    #Function for displaying the add student window
    def addStudent(self):
        #Sets the addStudent class to root2 so it is displayed when Add Instructor button is clicked
        root2 = Toplevel(self.master)
        AddStudent(root2)

    #Function for displaying the delete instructor window
    def deleteInstructor(self):
        #Sets the addInstructor class to root2 so it is displayed when Add Instructor button is clicked
        root2 = Toplevel(self.master)
        DeleteInstructor(root2)

    def addStudentCourse(self):
        #Sets the addInstructor class to root2 so it is displayed when Add Student to Course button is clicked
        root2 = Toplevel(self.master)
        AddStudentCourse(root2)

    #Function for displaying the searching window
    def search(self):
         #Sets the addInstructor class to root2 so it is displayed when Add Instructor button is clicked
        root2 = Toplevel(self.master)
        Search(root2)

