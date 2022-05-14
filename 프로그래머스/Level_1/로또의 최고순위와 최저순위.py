def solution(lottos, win_nums):
    answer = []

    winCount = 0
    zeroCount = 0

    for l in lottos:
        if l == 0:
            zeroCount = zeroCount+1
        elif win_nums.count(l) > 0:
            winCount = winCount+1


    max = getResult(winCount + zeroCount)
    min = getResult(winCount)

    answer.extend([max,min])

    return answer

def getResult(count):
    
    result = 6

    if count == 6:
        result = 1
    elif count == 5:
        result = 2
    elif count == 4:
        result = 3
    elif count == 3:
        result = 4
    elif count == 2:
        result = 5
    
    return result

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))