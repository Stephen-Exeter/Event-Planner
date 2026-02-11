
# --- MAIN FILE FOR THE EVENT PLANNER ---
# Contains :
#   - FinalOutput function
#   - __main__

#imports needed
from brute_force import Brute_Force
from dynamic_programming import Dynamic_Programming
from take_input import read_file
import timeit

def Final_Output(input_file):
    # gets variables no_of_events, hours_max, budget_max and the dict events
    no_events, hours_max, budget_max, events = read_file(input_file) 

    # runs the brute force algorithm for finding the max happiness

    no_events,hours_max,budget_max,events = read_file(input_file) 
    event_list_brute_force , enjoyment_brute_force , time_brute_force = Brute_Force(no_events,
                                                                                    hours_max,
                                                                                    budget_max,
                                                                                    events)
    
    # runs the dynamic programming algorithm for finding the max happiness
    event_list_dynamic , enjoyment_dynamic = Dynamic_Programming(no_events,
                                                                hours_max,
                                                                budget_max,
                                                                events)
    
    # print statemnent for all found values

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