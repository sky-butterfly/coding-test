def solution(myString, pat):
    answer = myString
    
    for i in range(len(myString), 0, -1):
        if myString[:i].endswith(pat):
            answer = myString[:i]
            break;
    
    return answer