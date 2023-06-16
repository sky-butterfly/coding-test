def solution(my_string):
    answer = []
    
    for i in range(65, 91) :
        answer.append(len(my_string)-len(my_string.replace(chr(i), '')))
                      
    for i in range(97, 123) :
        answer.append(len(my_string)-len(my_string.replace(chr(i), '')))
    
    return answer