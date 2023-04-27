def solution(num_list):
    answer = 0
    
    sum_result = 0
    multi_result = 1
    
    for n in num_list:
        sum_result += n
        multi_result *= n
    
    if (sum_result * sum_result) > multi_result:
        answer = 1
    
    return answer