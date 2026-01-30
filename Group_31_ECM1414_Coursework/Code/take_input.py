
# This is the function that allows us to accept the input from the text file, and splits it into the needed variables/arrays

# 1. Set chosen input file from the 3 possible ones
# 2. Take first 2 lines of the file, representing number of possible events, hours available and budget.
# 3. Save these values into variables to be returned
# 4. Create a dictionary for all the tasks 
# 5. Loop through all the remaining lines and add them to a dictionary
#   a. Read line into a variable
#   b. Split line into name, time_length, cost and happiness
#   c. Save into the dictionary with the name as the key and time_length, cost and happiness as its values
# 6. Return the 3 values and dictionary
#   a. Order is in no_of_events, max_hours, max_budget and event_dict

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
    file_lines = input_file.readlines()
    print(file_lines)

    # Reads the first 2 lines
    line1 = (file_lines[0])[:-1]
    line2 = (file_lines[1])[:-1]

    # Set needed variables

    no_of_events = int(line1)
    
    line2 = line2.split()

    max_hours = line2[0]
    max_budget = line2[1]

    # Create and add events to a dictionary

    event_dict = {}

    for a in range(2, no_of_events + 2):
        current_line = (file_lines[a])[:-1]
        current_line = current_line.split()

        current_line[1:] = [ int(x) for x in current_line[1:] ]

        event_dict[current_line[0]] = current_line[1:]

    return(no_of_events, max_hours, max_budget, event_dict)
