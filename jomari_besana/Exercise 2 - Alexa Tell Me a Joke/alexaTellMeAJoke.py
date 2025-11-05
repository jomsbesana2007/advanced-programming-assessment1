import random as r

# The program opens and reads the Jokes.txt file
with open(r"Exercise 2 - Alexa Tell me a Joke\Jokes.txt", encoding="UTF8") as jokes_f:
    # Strips \n characters and adds to clean_l list
    clean_l = [joke.strip() for joke in jokes_f if joke != '\n']

    # Splits the joke line into two which are separated by a '?'.
    # The first line is the setup and the second line is the punchline
    jokes = [x.split('?') for x in clean_l if '?' in x]

    # First while loop which executes until the user types the prompt, 'Alexa tell me a joke'
    while True:
        userPrompt = input("Type here 'Alexa tell me a joke' : ").strip()

        # '.lower()' is used to avoid issues with capitalisation
        if userPrompt.lower() == 'alexa tell me a joke':
            break
        # Runs when the user types something else
        else:
            print("I didn't understand.")
            continue
    
    # Initialises the alexaLoop with 'True' for it to run
    alexaLoop = True

    # Second while loop which executes until the user decides to exit the program
    while alexaLoop == True:
        # Chooses a random joke from the said jokes list
        chosenjoke = r.choice(jokes)
        
        # Prints the setup/question
        print(f"\n{chosenjoke[0]}?")

        # Asks the user to type 'why?' to show the punchline
        while True:
            userPrompt = input("\nType 'go on' : ").strip()

            if userPrompt.lower() == 'go on':
                break
            else:
                print("I didn't understand.")
                continue
        
        # Prints the punchline
        print(f"\n{chosenjoke[1].strip()}")
        
        # A nested while loop asking if the user wants to hear another joke
        while True:
            userPrompt = input("\nDo you want to tell another joke?\n'Y' for Yes and 'N' for No : ").strip()

            # Exits the program
            if userPrompt.lower() == 'n':
                alexaLoop = False # Ends the loop
                break # Breaks current loop
            # Continues the program
            elif userPrompt.lower() == 'y':
                break
            # Simple error handling feature
            else:
                print("I didn't understand.")
                continue # Continues current loop