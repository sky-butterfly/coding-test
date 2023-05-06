def solution(num_list):
    
    last = num_list[len(num_list)-1]
    frontOfLast = num_list[len(num_list)-2]
    
    if last > frontOfLast :
        num_list.append(last-frontOfLast)
    else :
        num_list.append(last*2)
    
    return num_list