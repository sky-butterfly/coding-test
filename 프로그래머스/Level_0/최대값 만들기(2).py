def solution(numbers):
    answer = 0
    
    numbers.sort()
    size = len(numbers)
    
    x = numbers[0] * numbers[1]
    y = numbers[size-1] * numbers[size-2]
    
    if x > y :
        answer = x
    else :
        answer = y
    
    return answer