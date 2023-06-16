def solution(my_string):
    answer = 0
    plus = '+'
    minus = '-'
    s = plus
    arr = my_string.split(' ')
    
    num = ''
    for i, a in enumerate(arr):
        
        if a.isdigit():
            num += a
            
            if i < len(arr)-1:
                continue
            
        if s == plus :
            answer += int(num)
        else:
            answer -= int(num)
        num = ''
        s = a
    
    return answer