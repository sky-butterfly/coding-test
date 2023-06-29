def solution(numbers):
    answer = []
    
    for num in numbers:
        x = (num^(num+1)) >> 2
        x += num
        x += 1
        answer.append(x)
    
    return answer
    
    