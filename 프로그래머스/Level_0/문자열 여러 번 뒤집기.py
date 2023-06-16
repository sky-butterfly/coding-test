def solution(my_string, queries):
    my_list = list(my_string)
    
    for q in queries:
        s = q[0]
        e = q[1]
        
        ml = my_list[s:e+1]
        ml.reverse()
        
        my_list[s:e+1] = ml
    
    return ''.join(my_list)