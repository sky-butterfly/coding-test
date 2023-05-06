def solution(num_list, n):
    answer = []
    index = 0
    
    for i, v in enumerate(num_list) :
        if i == index :
            answer.append(v)
            index+=n
    
    return answer