
# Need to install dependencies. Run line below in terminal
# pip install -r requirements.txt

import timeit
import matplotlib.pyplot as plt
from take_input import *
from brute_force import *
from dynamic_programming import *

"""
def example():
  link = "Group_31_ECM1414_Coursework/Input_Files"
  list = link.listdir()
  return list
print(example())
"""

def choose_input(): # getting data from all input files
  list = ["Group_31_ECM1414_Coursework/Input_Files/input_small.txt",
          "Group_31_ECM1414_Coursework/Input_Files/input_medium.txt",
          "Group_31_ECM1414_Coursework/Input_Files/input_large.txt",
          ]
  input = []
  for i in list:
    input.append(read_file(i))
  return input


def getting_data(): # replace tuples to lists in data from choose_input
  list_0 = []
  list_1 = []
  for i in choose_input():
    for k in i:
      list_1.append(k)
    list_0.append(list_1)
    list_1 = []
  return list_0


def brute_force_time(): # A function to find execution time for brute force algorithm
  time = []
  no_of_events = []

  for i in getting_data():
    no_of_events.append(i[0])

    start = timeit.timeit()
    Brute_Force(i[0], i[1], i[2], i[3])
    end = timeit.timeit()
    time.append(round(end - start, 6))

  return time, no_of_events


def dynamic_programming_time(): # A function to find execution time for dynamic programming algorithm
  time = []
  no_of_events = []

  for i in getting_data():
    no_of_events.append(i[0])

    start = timeit.timeit()
    Dynamic_Programming(i[0], i[1], i[2], i[3])
    end = timeit.timeit()
    time.append(round(end - start, 6))

  return time, no_of_events


# A function which creates a line graph comparing the execution time of brute force vs. dynamic programming as n increases (time on y-axis, n on x-axis)
def comparing_algorithms_line_graph(brute_force_time=brute_force_time()[0],
                                    dynamic_programming_time=dynamic_programming_time()[0],
                                    no_of_events=brute_force_time()[1]):
  
  plt.plot(no_of_events, brute_force_time, label="brute force")
  plt.plot(no_of_events, dynamic_programming_time, label="dynamic programming")

  plt.title("Comparing time spent on algorithms")
  plt.xlabel("Number of events")
  plt.ylabel("Time spent")

  plt.savefig('Group_31_ECM1414_Coursework/graphs/line_graph.png')

comparing_algorithms_line_graph()


# A function which creates a bar chart showing the "speedup factor" (brute force time ÷ dynamic programming time) for each input size.
def speedup_factor_bar_chart():
  pass





print(f"brute: {brute_force_time()}")
print(f"dynamic: {dynamic_programming_time()}")
