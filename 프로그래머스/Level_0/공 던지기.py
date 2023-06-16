def solution(numbers, k):
    answer = 0
    size = len(numbers)
    num = 0
    
    for i in range(1, k):
        num += 2
        answer = num%size + 1
    
    return answer