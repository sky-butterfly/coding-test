def solution(n, slicer, num_list):
    answer = []
    a = slicer[0]
    b = slicer[1]
    c = slicer[2]
    
    if n == 1:
        answer.extend(num_list[:b+1])
    elif n == 2:
        answer.extend(num_list[a:])
    elif n == 3:
        answer.extend(num_list[a:b+1])
    else:
        for i in range((b+1)-a):
            if i%c == 0:
                answer.append(num_list[a+i])
        
    
    return answer