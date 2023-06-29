from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for per in permutations(dungeons, len(dungeons)):
        kk = k
        cnt = 0
        for p in per:
            if kk < p[0]:
                break
            kk -= p[1]
            cnt += 1
        if answer < cnt:
            answer = cnt
    
    return answer
