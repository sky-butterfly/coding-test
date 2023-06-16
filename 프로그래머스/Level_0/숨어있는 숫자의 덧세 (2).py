def solution(my_string):
    answer = 0
    strNum = ''
    
    for m in my_string:
        if m.isdigit():
            strNum += m
        else :
            if strNum != '':
                answer += int(strNum)
                strNum = ''
    
    if strNum != '':
        answer += int(strNum)
    
    return answer