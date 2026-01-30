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
Dynamic_Programming(*read_file())

def Final_Output(input_file,):
    print(f"""Event Planner results
          
            -Available time:
            -Available budget:

            --Brute Force ALgorithm--
          
            Selected Activities:
                ...
          
            Total enjoyment:
                ...
          
            Execution Time:
                {timeit.timeit("Brute_Force()","from __main__ import Brute_Force",number=10)/10} (average from 10 calls)


            -Dynamic Programming Algorithm-

            Selected Activities:
                ...

            Total Enjoyment:
                ...
                
            Execution Time:
                {timeit.timeit("Dynamic_Programming()","from __main__ import Dynamic_Programming",number=10)/10} (average from 10 calls)
            """)
if __name__ == "__main__":
    # Final_Output()
    ...