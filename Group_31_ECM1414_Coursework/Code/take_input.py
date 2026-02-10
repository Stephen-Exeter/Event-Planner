
# This is the function that allows us to accept the input from the text file, and splits it into the needed variables/arrays

# 1. Take first 2 lines of the file, representing number of possible events, hours available and budget.
# 2. Save these values into variables to be returned
# 3. Create a dictionary for all the tasks 
# 4. Loop through all the remaining lines and add them to a dictionary
#   a. Read line into a variable
#   b. Split line into name, time_length, cost and happiness
#   c. Save into the dictionary with the name as the key and time_length, cost and happiness as its values
# 5. Return the 3 values and dictionary
#   a. Order is in no_of_events, max_hours, max_budget and event_dict

def read_file(chosen_input_file):

    # Opens the file
    input_file = open(chosen_input_file, 'r')
    file_lines = input_file.readlines() #puts each line as an item in an array

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

    for a in range(2, no_of_events + 2): #loop for each dictionary addition
        current_line = (file_lines[a])[:-1] #gets the current line minus the /n on the end
        current_line = current_line.split()

        current_line[1:] = [ int(x) for x in current_line[1:] ] # turns each value other than the activity name into an integer

        event_dict[current_line[0]] = current_line[1:] #adds to the dictionary

    return(no_of_events, max_hours, max_budget, event_dict)

#for testing purposes
#read_file("Group_31_ECM1414_Coursework/Input_Files/input_small.txt")
