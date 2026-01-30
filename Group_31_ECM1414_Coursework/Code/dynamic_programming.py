def Dynamic_Programming(num_events,max_hours,max_budget,event_dict):

    # first idea of how this should work
    # consider as if you were doing all of the activities at first
    # find a value such as enjoyment/time or budget to show which activity is the most efficient for enjoyment
    # ignore the least efficient value and stop doing future considerations for that part of the table
    # store all of the efficiency values so don't need to recalculate how efficient each activity is
    # henceforth use the efficiency values and pick the most efficient each time? Doesn't seem like it would be what they want
    # try using stacks or queues
    # 
    # just use Dijkstra's algorithm idk how with 2/3 varibales to consider but \_()_/ 

    list_set_of_activities = []
    table = [[],   # make the number of lists within the list the number of activities
             []]
    
    activities = ...
    total_enjoyment = ...
    return {"selected_activities":activities,
            "total enjoyment":total_enjoyment}