def solution(number, limit, power):
    answer = 0
    
    for i in range(1, number+1):
        cnt = get(i, limit)
        if cnt > limit:
            cnt = power
        answer += cnt
    
    return answer

def get(num, limit):
    count = 0
    if num == 1:
        return 1
    size = int(num**0.5) + 1
    for i in range(1, size):
        if num%i == 0:
            if i == num**0.5:
                count += 1
            else:
                count += 2
        if count > limit:
            break
    return count