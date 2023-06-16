def solution(myStr):
    answer = []
    answer2 = []
    
    arr = myStr.split('a')
    
    for a in arr:
        answer.extend(a.split('b'))
    
    for a in answer:
        answer2.extend(a.split('c'))
    
    answer2 = [i for i in answer2 if i != '']
    
    if len(answer2) == 0:
        answer2.append('EMPTY')
    
    return answer2