
# This is the function that allows us to accept the input from the text file, and splits it into the needed variables/arrays

# 1. Set chosen input file from the 3 possible ones
# 2. Take first 2 lines of the file, representing number of possible events, hours available and budget.
# 3. Save these values into variables to be returned
# 4. Create a dictionary for all the tasks 
# 5. Loop through all the remaining lines and add them to a dictionary
#   a. Read line into a variable
#   b. Split line into name, time_length, cost and happiness
#   c. Save into the dictionary with the name as the key and time_length, cost and happiness as its values
# 6. Return the 2 values and dictionary

def read_file():

    chosen_input_file = ''

    # While loop for valid input for file choice
    while chosen_input_file == '':
        file_choice = input("Would you like to us the smalle [S], medium [M] or large [L] input file? : ")
        if file_choice.upper() == 'S':
            chosen_input_file = "Group_31_ECM1414_Coursework/Input_Files/input_small.txt"
        elif file_choice.upper() == 'M':
            chosen_input_file = "Group_31_ECM1414_Coursework/Input_Files/input_medium.txt"
        elif file_choice.upper() == 'L':
            chosen_input_file = "Group_31_ECM1414_Coursework/Input_Files/input_large.txt"
        else :
            print("Not chosen a valid file to open")

    # Opens the file
    input_file = open(chosen_input_file, 'r')

    # Reads the first 2 lines
    line1 = input_file.readline()
    line2 = input_file.readline()

    # Set needed variables

    no_of_events = int(line1)
    
    line2 = line2.split()
    print(line2)

    max_hours = line2[0]
    max_budget = line2[1]

    print(no_of_events, max_hours, max_budget)

    

read_file()