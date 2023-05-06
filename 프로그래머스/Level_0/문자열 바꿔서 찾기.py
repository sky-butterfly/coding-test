def solution(myString, pat):
    answer = 0
    
    myString = myString.replace('A', 'N').replace('B', 'M').replace('N', 'B').replace('M', 'A')
    
    if pat in myString :
        answer = 1
    
    return answer