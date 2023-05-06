def solution(array):
    answer = []
    maxvalue = array[0]
    maxindex = 0
    
    for i, a in enumerate(array):
        if maxvalue < a:
            maxvalue = a
            maxindex = i
    
    answer.append(maxvalue)
    answer.append(maxindex)
    
    return answer