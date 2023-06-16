def solution(s):
    answer = 0
    arr = s.split(' ')
    before = 0
    
    for a in arr:
        if a.isdigit() or a.startswith('-'):
            answer += int(a)
            before = int(a)
            continue
        answer -= int(before)
    
    return answer