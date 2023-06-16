def solution(my_string):
    answer = []
    
    for m in my_string:
        if m in answer:
            continue
        answer.append(m)
    
    return ''.join(answer)