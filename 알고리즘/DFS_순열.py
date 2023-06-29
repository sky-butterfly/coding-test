from itertools import permutations

def solution(k, dungeons):
    
    for per in permutations(dungeons, len(dungeons)):
        for p in per:
            print(p)
    
    return answer
