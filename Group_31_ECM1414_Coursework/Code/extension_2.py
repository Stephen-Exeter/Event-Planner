import timeit
from take_input import *
from brute_force import *
from dynamic_programming import *

# A function to find execution time for brute force algorithm

def brute_force_time():
  start = timeit.timeit()
  Brute_Force(read_file())
  end = timeit.timeit()
  return end - start


# A function to find execution time for dynamic programming algorithm

def dynamic_programming_time():
  start = timeit.timeit()
  Dynamic_Programming(read_file())
  end = timeit.timeit()
  return end - start


# A function which creates a line graph comparing the execution time of brute force vs. dynamic programming as n increases (time on y-axis, n on x-axis)

def comparing_algorithms_line_graph():
  pass


# A function which creates a bar chart showing the "speedup factor" (brute force time ÷ dynamic programming time) for each input size.

def speedup_factor_bar_chart():
  pass
