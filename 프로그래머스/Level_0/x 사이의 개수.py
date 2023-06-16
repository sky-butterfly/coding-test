def solution(myString):
    answer = []
    
    arr = myString.split('x')
    
    for a in arr:
        answer.append(len(a))
    
    return answer