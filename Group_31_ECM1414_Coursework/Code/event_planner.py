# Who up planning they events

#hello

# CONSTRAINT BEING CODED FIRST : TIME


# CONSTRAINT BEING CODED FIRST : TIME

from brute_force import Brute_Force
from dynamic_programming import Dynamic_Programming
from take_input import read_file
import timeit

# def BruteForce(Constraint, InputData):
#     maxHappiness = 0
#     #loop through each combo, find max happiness
#     #if max happiness is higher than current highest, replace
#     pass

# def DynamicAlgor():
#     pass

#just runnning it here for testing
# Dynamic_Programming(*read_file())

def Final_Output(input_file):

    no_events,hours_max,budget_max,events = read_file(input_file) 
    event_list_brute_force , enjoyment_brute_force , time_brute_force = Brute_Force(no_events,
                                                                                    hours_max,
                                                                                    budget_max,
                                                                                    events)
    event_list_dynamic , enjoyment_dynamic = Dynamic_Programming(no_events,
                                                                hours_max,
                                                                budget_max,
                                                                events)



    print(f"""Event Planner results
          
            -Available time: {hours_max}
            -Available budget: {budget_max}

            --Brute Force ALgorithm--
          
            Selected Activities:
                {event_list_brute_force}
          
            Total enjoyment:
                {enjoyment_brute_force}
          
            Execution Time:
                {timeit.timeit(lambda : Brute_Force(*read_file(input_file)),
                               number=10)/10} (average from 10 calls)


            -Dynamic Programming Algorithm-

            Selected Activities:
                {event_list_dynamic}

            Total Enjoyment:
                {enjoyment_dynamic}
                
            Execution Time:
                {timeit.timeit(lambda : Dynamic_Programming(*read_file(input_file)),
                               number=10)/10} (average from 10 calls)
            """)
if __name__ == "__main__":
    Final_Output(r"Group_31_ECM1414_Coursework\Input_Files\input_small.txt")
    Final_Output(r"Group_31_ECM1414_Coursework\Input_Files\input_medium.txt")
    Final_Output(r"Group_31_ECM1414_Coursework\Input_Files\input_large.txt")


    # file_path = input("Input the file path to the input file")
    # Final_Output(file_path)