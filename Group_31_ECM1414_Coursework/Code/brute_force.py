def Brute_Force(eventCount, totalTime, totalCost, inputData):
    
    # Define eventCount, totalTime, event, timeConstraint, happiness
    # take total number of events
    # define max possible happiness
    # organise each combination of events sticking to restictions
    # try get as close to max happiness as possible within totalTime
    # Outputs best combination, total enjoyment reached

    events = inputData
    output_enjoyment = 0
    
    tempHappiness = 0
    
    for key in events.keys():
        tempTime = int(totalTime)
        tempList = [key]
        tempHappiness = int(events.get(key)[2])
        
        for key2 in events.keys():
            if key2 != key:
                if tempTime >= int(events.get(key2)[0]):
                    tempTime -= int(events.get(key2)[0])
                    tempList.append(key2)
                    tempHappiness += int(events.get(key2)[2])
        
        if tempHappiness > output_enjoyment:
            output_list = tempList
            output_enjoyment = tempHappiness
            output_time = int(totalTime) - tempTime

    for i in range(len(output_list)):
        data = [output_list[i], events.get(output_list[i])]
        output_list[i] = data

    # extension: stick to both time and cost constraints
    return output_list, output_enjoyment, output_time