def solution(number):
    
    sum = 0
    
    for n in number:
        sum += int(n)
    
    return sum%9