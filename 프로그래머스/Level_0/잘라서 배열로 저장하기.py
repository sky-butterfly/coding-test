def solution(my_str, n):
    answer = []
    size = len(my_str)
    limit = int(size/n)
    if size%n > 0:
        limit += 1
    
    for i in range(limit):
        if (i*n)+n >= size:
            answer.append(my_str[i*n:])
            continue
        answer.append(my_str[i*n:i*n+n])
    
    return answer