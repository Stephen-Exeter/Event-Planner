import timeit
import matplotlib.pyplot as plt
from take_input import *
from brute_force import *
from dynamic_programming import *

# A function to find execution time for brute force algorithm

def brute_force_time():
  start = timeit.timeit()
  Brute_Force(read_file())
  end = timeit.timeit()
  no_of_events = read_file()[0]
  return end - start, no_of_events


# A function to find execution time for dynamic programming algorithm

def dynamic_programming_time():
  start = timeit.timeit()
  Dynamic_Programming(read_file())
  end = timeit.timeit()
  no_of_events = read_file()[0]
  return end - start, no_of_events


# A function which creates a line graph comparing the execution time of brute force vs. dynamic programming as n increases (time on y-axis, n on x-axis)

def comparing_algorithms_line_graph(brute_force_time,
                                    dynamic_programming_time,
                                    no_of_events):
  
  plt.plot(no_of_events, brute_force_time)
  plt.plot(no_of_events, dynamic_programming_time)

  plt.savefig('Group_31_ECM1414_Coursework/graphs/line_graph.png')
comparing_algorithms_line_graph([1, 4, 8], [2, 5, 7], [1, 2, 3])

# A function which creates a bar chart showing the "speedup factor" (brute force time ÷ dynamic programming time) for each input size.

def speedup_factor_bar_chart():
  pass
