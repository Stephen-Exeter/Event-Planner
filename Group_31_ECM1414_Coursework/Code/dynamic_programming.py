def Dynamic_Programming(num_events:int ,max_hours:str ,max_budget:str ,event_dict:dict) -> list:

    table = [[[],0] for _ in range(int(max_hours) + 1)] #all amounts of time possible
                                                        #and the +1 to store the final result
    
    for name, list_vals in event_dict.items():
        time,cost,enjoyment = list_vals
        
        for hours in range(int(max_hours),time-1,-1):
            hours_left = hours - time
            
            if table[hours_left][1] + enjoyment > table[hours][1]:
                table[hours][0] = table[hours_left][0] + [name] # keep track of which events have been chosen on path
                table[hours][1] = table[hours_left][1] + enjoyment # the total enjoyment of those chosen events

    return table[int(max_hours)]   # returned list will be [ [events selected] , total enjoyment ]