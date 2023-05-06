def solution(my_string, num1, num2):
    
    toList = list(my_string)
    toList[num1] = my_string[num2]
    toList[num2] = my_string[num1]
    
    return ''.join(toList)