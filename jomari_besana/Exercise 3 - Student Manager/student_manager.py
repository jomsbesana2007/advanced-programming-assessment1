from tkinter import *
from tkinter.ttk import *

window = Tk() # Creates a main window
window.title('Student Manager')
window.geometry('900x700')
window.resizable(0,0) # Prevents users from resizing the window
window['bg'] = "#DBDBDB"

# Reads Marks.txt file and imports data into the program
def readfile():
    # Opens the file
    with open(r"Exercise 3 - Student Manager\Marks.txt", encoding="UTF-8") as f:
        studentsRecords = [] # Empty list to store dictionaries containing information and records of each student
        grading = {'A': (70, 100), 'B': (60, 69), 'C': (50, 59), 'D': (40, 49), 'F': (0, 39)} # To categorise students' grades
        cleaned_f = [i.strip() for i in f if i != '\n'] # Removes any '\n' characters
        
        for student in cleaned_f:
            # Splits the data combined into one string (e.g., ["1001, Ava Williams, 13,15,17,70"]) into usable data by ',')
            s_list = [s.strip() for s in student.split(',')]

            # Creates a dictionary containing information about each student
            s_info = {}

            # Adds keys and their values. Assessed elements from s_list are assigned to these keys as values
            s_info["ID"] = s_list[0] 
            s_info["Name"] = s_list[1]
            s_info["Coursework Total"] = int(s_list[2]) + int(s_list[3]) + int(s_list[4])
            s_info["Exam Score"] = f"{int(s_list[5])}%"

            # Grades the final exam scores
            for grade, (min, max) in grading.items(): # for reference: {'A': (70, 100)}
                if min <= int(s_list[5]) <= max: # Checks if the student's grade is within a specified range
                    s_info["Grade"] = grade # The student's grade is assigned to the "Grade" key as a value
            
            # Informaton about the student, stored in dictionaries, is appended to the studentsList
            studentsRecords.append(s_info) 

        # Returns the full list with the dictionaries after the for loop ends
        return studentsRecords
    
# studentRecords refers to the return value of readfile(), which is studentsRecords.
# Therefore the variable stores the full list and can be used in the rest of the program
studentsRecords = readfile()

# Tkinter Styles
s = Style() # A class that allows for styling
s.configure('Title.TLabel', font=('Arial', 30, 'bold'), background="#DBDBDB")
s.configure('TLabel', font=('Arial', 15), background="#DBDBDB")
s.configure('TButton', font=('Arial', 12), background="#DBDBDB")
s.configure('TText', font=('Arial', 12), background="#DBDBDB")
s.configure('Exit.TButton', font=('Arial', 12, 'bold'), foreground="#BB1F1F")
s.configure('TFrame', background="#DBDBDB")

# Title frame
titleFrame = Frame(window)
titleFrame.pack(pady=20)

title = Label(titleFrame, text="Student Manager", justify="center", style="Title.TLabel")
title.pack(pady=20)

# Creates three button grid frame
grid1 = Frame(window)
grid1.pack(pady=20)

# View individual student record grid frame
grid2 = Frame(window)
grid2.pack(pady=20)

# Textbox frame
grid3 = Frame(window)
grid3.pack(pady=20)

# Creates a Text widget to display the records
txtBox = Text(grid3, height=20, width=80, font=('Arial', 12)) # style is not a supported parameter for Text widget
txtBox.config(state=NORMAL) # Means Text widget can be edited
txtBox.pack(padx=20, pady=20)

# Allows the user to view all records
def viewAllRecords():
    txtBox.delete('1.0', END) # Erases content in the Text widget before displaying other info
    for s in studentsRecords:
        allRecords = f"ID : {s["ID"]}\nName : {s["Name"]}\nCoursework Total : {s["Coursework Total"]}\nExam Score : {s["Exam Score"]}\nFinal Grade : {s["Grade"]}\n\n"
        txtBox.insert(END, allRecords) # Adds text in the widget

# Button that executes the viewAllRecords function
btn1 = Button(grid1, text="View All Student Records", command=viewAllRecords)
btn1.grid(row=0, column=1, sticky=W, padx=20, ipadx=25, ipady=10)

# Allows the user to view the student(s) with the highest marks
def showHighestMark():
    txtBox.delete('1.0', END) 
    examScores = [s["Exam Score"] for s in studentsRecords] # Appends all the scores of each student
    highestScore = max(examScores) # Finds the highest score from the list and stores it in highestScore

    for s in studentsRecords:
        if highestScore == s["Exam Score"]: # Checks if the highest score in the list belongs to a particular student so that their information is correctly printed
            studentHighest = f"ID : {s["ID"]}\nName : {s["Name"]}\nCoursework Total : {s["Coursework Total"]}\nExam Score : {s["Exam Score"]}\nFinal Grade : {s["Grade"]}\n\n"
            txtBox.insert(END, studentHighest)

# Button that executes the showHighestMark function
btn2 = Button(grid1, text="Show Highest Mark", command=showHighestMark)
btn2.grid(row=0, column=2, sticky=EW, padx=20, ipadx=25, ipady=10)

# Allows the user to view the student(s) with the highest marks
def showLowestMark():
    txtBox.delete('1.0', END)
    examScores = [s["Exam Score"] for s in studentsRecords] # A list containing all of the exam scores
    lowestScore = min(examScores) # Finds the lowest score from the list and stores it in lowestScore
    
    for s in studentsRecords:
        if lowestScore == s["Exam Score"]: # Checks if the lowest score in the list belongs to a particular student
            studentLowest = f"ID : {s["ID"]}\nName : {s["Name"]}\nCoursework Total : {s["Coursework Total"]}\nExam Score : {s["Exam Score"]}\nFinal Grade : {s["Grade"]}\n\n"
            txtBox.insert(END, studentLowest)

# Button that executes the showLowestMark function
btn3 = Button(grid1, text="Show Lowest Mark", command=showLowestMark)
btn3.grid(row=0, column=3, sticky=EW, padx=20, ipadx=25, ipady=10)

# Allows the user to view a student's particular records
def viewIndividualRecord():
    txtBox.delete('1.0', END)
    for s in studentsRecords:
        # Checks if the name of the student the user chose matches.
        if chosenName.get() == s["Name"]:
            individualRecord = f"ID : {s["ID"]}\nName : {s["Name"]}\nCoursework Total : {s["Coursework Total"]}\nExam Score : {s["Exam Score"]}\nFinal Grade : {s["Grade"]}\n\n"
            txtBox.insert(END, individualRecord)

# Label
l1 = Label(grid2, text="View Individual Student Record")
l1.grid(row=0, column=1, sticky=W, padx=20)

chosenName = StringVar() # Retrieves the string value from 'dropdown' Combobox widget based on the name the user chose
names = [s['Name'] for s in studentsRecords] # Only stores all the names to be displayed in the widget
dropdown = Combobox(grid2, values=names, textvariable=chosenName)
dropdown.set("Select a student")
dropdown.grid(row=0, column=2, sticky=EW, padx=20, ipady=10, ipadx=10)

# Button that executes the viewIndividualRecord function
btn4 = Button(grid2, text="View Record", command=viewIndividualRecord)
btn4.grid(row=0, column=3, sticky=E, padx=20, ipadx=25, ipady=10)

# To exit the application
def exitApp():
    window.destroy() # Ends the process when the user clicks on the exit button

exitbtn = Button(window, text="Exit", command=exitApp, style="Exit.TButton")
exitbtn.place(x=10, y=10)

# An infinite loop which will run until the user exits the app
window.mainloop()