def Dynamic_Programming(num_events:int ,max_hours:str ,max_budget:str ,event_dict:dict):

    table = [[[],0] for _ in range(int(max_hours) + 1)] #all amounts of time possible
                                                        #and the +1 to store the final result
    
    for name, list_vals in event_dict.items():
        time,cost,enjoyment = list_vals
        print(name)
        for hours in range(int(max_hours),time-1,-1):
            hours_left = hours - time
            print(hours_left)
            
            if table[hours_left][1] + enjoyment > table[hours][1]:
                table[hours][0] = table[hours_left][0] + [name]
                table[hours][1] = table[hours_left][1] + enjoyment

    print(table[int(max_hours)])

    return table[int(max_hours)]