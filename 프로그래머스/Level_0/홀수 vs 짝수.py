def solution(num_list):
    answer = 0
    even = 0
    odd = 0
    
    for i, v in enumerate(num_list):
        if (i+1)%2 == 0:
            even += v
            continue
        odd += v
    
    if even > odd :
        answer = even
    else :
        answer = odd
    
    return answer