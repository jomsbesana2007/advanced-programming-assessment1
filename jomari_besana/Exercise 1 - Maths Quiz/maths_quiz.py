import random as r
import operator as op

# FUNCTIONS

# Displays the menu of all difficulties the user can choose from
def displayMenu():
    # While loop that continues running when the user enters an erroneous entry
    while True:
        print("SELECT DIFFICULTY LEVEL\n1 - Easy\n2 - Moderate\n3 - Advanced")
        userChoice = input('Enter here : ')
        print(" ") # Spacing
        choices = ['1', '2', '3']
        if userChoice not in choices:
            continue
        else:
            return userChoice.strip()

# Random number generator which randomly chooses a number based on difficulty
def randomInt(difficulty):
    # Easy difficulty
    if difficulty == '1':
        x = r.randint(1, 9)
        y = r.randint(1, 9)
    # Moderate difficulty
    elif difficulty == '2':
        x = r.randint(10,99)
        y = r.randint(10,99)
    # Advanced difficulty
    elif difficulty == '3':
        x = r.randint(1000,9999)
        y = r.randint(1000,9999)
    return x,y

# Decides an operation randomly 
def decideOperation():
    # A dictionary of all the operator module functions (e.g., op.add) and operators (e.g., '+')
    operations = {op.add: '+', op.sub: '-'}
    # .choice() function is used to randomly choose an operation from the dictionary
    operation, operator = r.choice(list(operations.items()))

    # operation - returns the operator module function that was chosen randomly
    # operator - returns the string version of the operator to print in the problem
    return operation, operator

# Displays the problem for the user to solve
def displayProblem(problem, correctAns):
    # Initialises the number of attempts
    attempts = 1

    # Loop executes two times as the user is only given 2 attempts
    while attempts <= 2:
        print(f"Attempts: {attempts}")
        print(problem)
        userAns = int(input("Answer : "))
        print(" ") # Spacing

        # Returns user's answer and attempts if answer is correct
        if userAns == correctAns:
            return userAns, attempts
        
        # Updates number of attempts
        attempts += 1

    # Returns the user's last answer and total attempts when user fails to answer correctly twice
    return userAns, attempts

# Determines the number of points that will be given to the user based on how many attempts they took
def isCorrect(userAns, correctAns, attempts):
    # Checks both the user's answer and the number of attempts to give the right amount of points
    if userAns == correctAns and attempts == 1:
        print(f"Correct! the answer is {correctAns}, you got 10 points!")
        addPts = 10
    elif userAns == correctAns and attempts == 2:
        print(f"Correct! the answer is {correctAns}, you got 5 points")
        addPts = 5
    elif attempts > 2:
        print(f"Sorry, the answer is {correctAns}. You can try again in the next question")
        addPts = 0
    return addPts

# Displays the user's grade based on how many points they attained
def displayResults(userPts):
    # Grading rules
    grades = {"A": (70,100), "B": (60,69), "C": (50,59), "D": (40, 49), "F": (0,39)}
    for grade, (minPts, maxPts) in grades.items():
        # Checks if the user's total score is within the range of a category (e.g., if userPts = 60, grade = B)
        if minPts <= int(userPts) <= maxPts:
            return f"Total Score : {userPts} | Grade: {grade}"

# MAIN PROGRAM

questionNumber = 1 # Starts with 1 as it is the first question
userPts = 0 # User starts with zero points

# Loop ends when questionNumber = 11, falsifying the condition as there are only 10 questions
while questionNumber <= 10:
    # Beginning of the program, where the value of questionNumber is set to 1
    if questionNumber == 1:
        chosenDifficulty = displayMenu()

    # CHOOSING NUMBERS AND OPERATIONS RANDOMLY
    x, y = randomInt(chosenDifficulty) # Retrieves the numbers that were chosen randomly using randint() function
    operation, operator = decideOperation() # Retrieves operation (the module function) and operator (the string form)

    # DISPLAYING THE PROBLEM AND USER ANSWERS THE PROBLEM
    problem = f"[{questionNumber}] {x} {operator} {y}" # The written form of the problem
    correctAns = operation(x,y) # Refers to the correct answer
    userAns, attempts = displayProblem(problem, correctAns) # Displays the problem

    # ADDING POINTS
    addPts = isCorrect(userAns, correctAns, attempts) 
    userPts += addPts # Updates the total points

    print(f"Current Amount of Points : {userPts}\n") # Displays total points

    questionNumber += 1 # Updates as user progresses

    # END OF QUIZ
    if questionNumber == 11:  # End of the program once questionNumber = 11
        userGrade = displayResults(userPts) # Displays result
        print(userGrade)
        retry = input("Do you wanna play again?\n'Y' for Yes, 'N' for No : ").strip()
        print(" ") # Spacing

        if retry.lower() == 'y':
            # Resets stats to their original state
            questionNumber = 1 # Sets the value to 1 for the loop to restart again
            userPts = 0
        elif retry.lower() == 'n':
            break # Ends the program