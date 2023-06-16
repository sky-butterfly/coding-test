def solution(num, total):
    answer = []
    
    add = 0
    for n in range(num):
        add += n
        
    start = total - add
    if start != 0:
        start = int(start/num)
    
    for i in range(num):
        answer.append(start + i)
    
    return answer