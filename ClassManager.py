__author__ = 'Andre'

from tkinter import messagebox
from tkinter import *
import sqlite3

'''
Beginning example code for time manager
'''


# create a connection to the newly made database
cxn = sqlite3.connect('GymDB')
# initialize a cursor object to run execute commands on the connected database.
cur = cxn.cursor()

# start a try-except block to handle SQL-Exceptions
# create the table and fill it with data
try:
    cur.execute('CREATE TABLE Instructor(id INTEGER PRIMARY KEY, firstName VARCHAR(50), lastName VARCHAR(50), address VARCHAR(50))')
    cur.execute('CREATE TABLE Class(code VARCHAR(8) PRIMARY KEY, description VARCHAR(50), price FLOAT, instructorID INTEGER REFERENCES Instructor(id))')
    cur.execute('CREATE TABLE Schedule(code VARCHAR(8) REFERENCES Class(code), Day TEXT, time TEXT)')
    cur.execute('CREATE TABLE Student(id INTEGER PRIMARY KEY, firstName VARCHAR(50), lastName VARCHAR(50), address VARCHAR(50), amountDue FLOAT)')
    cur.execute('CREATE TABLE ClassStudent(code VARCHAR(8) REFERENCES Class(code), sequence INTEGER, studentID INTEGER REFERENCES Student(id))')
except sqlite3.OperationalError:
    print("The tables have been created already")

# Create some test data
try:
    def insert():
        cur.execute('INSERT INTO Instructor VALUES(NULL, "Bob", "Smith", "1234 Street")')
        cur.execute('INSERT INTO Class VALUES("Weight", "Lifting weights", 250.00, 1)')
        cur.execute('INSERT INTO Schedule VALUES("Weight", "Monday", "19:00")')
        cur.execute('INSERT INTO ClassStudent VALUES("Weight", 1, 1)')
        cur.execute('INSERT INTO Student VALUES(NULL, "Jane", "Smith", "1500 Tree Rd.", 0)')
except sqlite3.IntegrityError:
    print("Test data has been put in already")

#  To retrieve data after executing a SELECT statement, you can either treat the cursor as an iterator,
#  call the cursor’s fetchone() method to retrieve a single matching row, or call fetchall() to get a list of the matching rows.
'''try:
    cur.execute('SELECT * FROM Instructor')
    for eachUser in cur.fetchall():
        print("Successfully created the users table.")
        print(eachUser)

    cur.execute('SELECT * FROM Class')
    for eachUser in cur.fetchall():
        print("Successfully created the users table.")
        print(eachUser)

    cur.execute('SELECT * FROM Schedule')
    for eachUser in cur.fetchall():
        print("Successfully created the users table.")
        print(eachUser)

    cur.execute('SELECT * FROM ClassStudent')
    for eachUser in cur.fetchall():
        print("Successfully created the users table.")
        print(eachUser)

    cur.execute('SELECT * FROM Student')
    for eachUser in cur.fetchall():
        print("Successfully created the users table.")
        print(eachUser)
    # handle an sql exception if the table already exists
except sqlite3.OperationalError:
    print("Could not retrieve data")'''

'''# Final block runs always so that if something went wrong we can at least close the connection and commit whatever went through
finally:
    cur.close()
    cxn.commit()
    cxn.close()'''




#Class for the Main Window
class MainWindow():

    def __init__(self, master):

            #sets window to master, sets title, and window size
            self.master = master
            self.master.title("Class Manager")
            self.master.geometry("230x150")

            #Declares and defines labels, buttons, and textboxes
            self.btnAddInstructor = Button(self.master, text="Add Instructor", width=13, command=self.addInstructor)
            self.btnSearch = Button(self.master, text="Search", width=13, command=self.search)
            self.btnQuit = Button(self.master, text="Quit", width=13, command=self.quit)

            #Aligns all of the labels, buttons, and textboxes in grid form
            self.btnAddInstructor.grid(row=1, column=1, sticky=W)
            self.btnSearch.grid(row=2, column=1, sticky=W)
            self.btnQuit.grid(row=3, column=1)

    #Function for quit button to close window
    def quit(self):
        self.master.destroy()

    #Function for displaying the add instructor window
    def addInstructor(self):
        #Sets the addInstructor class to root2 so it is displayed when Add Instructor button is clicked
        root2 = Toplevel(self.master)
        AddInstructor(root2)

    #Function for displaying the searching window
    def search(self):
         #Sets the addInstructor class to root2 so it is displayed when Add Instructor button is clicked
        root2 = Toplevel(self.master)
        Search(root2)





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
        try:
            cur.execute('INSERT INTO Instructor VALUES(NULL, ?, ?, ?)', (first, last, address,))
            messagebox.showwarning("New Instructor Added", "New Instructor successfully added")

        except sqlite3.IntegrityError:
            messagebox.showwarning("New Instructor could not be added")

        finally:
            #cur.close()
            cxn.commit()
            #cxn.close()

#Class for searching for instructors, times, or classes
class Search:

    #myMainWindowClass = MainWindow(empName)
    def __init__(self, master):
        #creates master window for calculation window, changes title, and sets size
        self.master = master
        self.master.title("Search")
        self.master.geometry("250x200")

        #Sets the string variable and checkBox variables
        self.userSearchInput = StringVar()
        self.chkVar1 = IntVar()
        self.chkVar2 = IntVar()
        self.chkVar3 = IntVar()

        #Widgets
        self.chkBtnInstructorName = Checkbutton(self.master, text="Instructor Last Name", variable=self.chkVar1, justify=LEFT)
        self.chkBtnClassName = Checkbutton(self.master, text="Class Name", variable=self.chkVar2, justify=LEFT)
        self.chkBtnClassDay = Checkbutton(self.master, text="Class Day", variable=self.chkVar3, justify=LEFT)
        self.lblSearchInformation = Label(self.master, text="Search For Instructor, Classes, or schedules")
        self.lblSearch = Label(self.master, text="Search: ")
        self.txtBoxSearch = Entry(self.master, textvariable=self.userSearchInput)

        #Search Button
        self.btnSearch = Button(self.master, text="Search", width=12, command=self.searchQuery)
        #Close Button
        self.btnClose = Button(self.master, text="Close", width=12, command=self.quit)

        #Aligns the labels using the grid
        self.lblSearchInformation.grid(row=1, columnspan=1, sticky=W)
        self.chkBtnInstructorName.grid(row=2, columnspan=1, sticky=W)
        self.chkBtnClassName.grid(row=3, columnspan=1, sticky=W)
        self.chkBtnClassDay.grid(row=4, columnspan=1, sticky=W)
        self.lblSearch.grid(row=5, columnspan=1, sticky=W)
        self.txtBoxSearch.grid(row=6, columnspan=1, sticky=W)
        self.btnSearch.grid(row=7, columnspan=1, sticky=W)
        self.btnClose.grid(row=8, columnspan=1, sticky=W)

    #Searh Query Function
    def searchQuery(self):
        self.userSearchCriteria = self.userSearchInput.get()

        if(self.userSearchCriteria == ""):
            messagebox.showerror("Entry Error", "Textbox cannot be empty")
        else:
            try:
                #Gets the state of the checkboxes and then searches with the user input
                if(self.chkVar1.get()):
                    cur.execute("SELECT * FROM Instructor WHERE lastName LIKE ?", (self.userSearchCriteria,))
                    messagebox.showwarning("Query Results", cur.fetchall())

                elif(self.chkVar2.get()):
                    cur.execute("SELECT * FROM Class WHERE code LIKE ?", (self.userSearchCriteria,))
                    messagebox.showwarning("Query Results", cur.fetchall())

                elif(self.chkVar3.get()):
                    cur.execute("SELECT * FROM Schedule WHERE Day LIKE ?", (self.userSearchCriteria,))
                    messagebox.showwarning("Query Results", cur.fetchall())

            except sqlite3.IntegrityError:
                messagebox.showwarning("Search Error", "No matches could be found")

            finally:
                cxn.commit()

    def quit(self):
        self.master.destroy()

##Creates the root window and loops it
def main():
    root = Tk()
    MainWindow(root)
    root.mainloop()

#Loops the code so the windows stay open
if __name__ == "__main__":
    main()