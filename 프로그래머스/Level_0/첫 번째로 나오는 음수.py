def solution(num_list):
    answer = -1
    
    for i, v in enumerate(num_list) :
        if 0 > v:
            return i
    
    return answer