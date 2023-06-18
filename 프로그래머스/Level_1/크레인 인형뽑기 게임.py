def solution(board, moves):
    answer = 0
    obj = {}
    bag = []
    
    for i, bo in enumerate(board):
        for j, b in enumerate(bo):
            if j in obj.keys():
                if b == 0:
                    continue
                arr = obj[j]
                arr.append(b)
                obj[j] = arr
                continue
            if b == 0:
                obj[j] = []
            else:
                obj[j] = [b]
    
    for m in moves:
        arr = obj[m-1]
        if len(arr) < 1:
            continue
        a = arr.pop(0)
        if len(bag) > 0:
            if bag[len(bag)-1] == a:
                bag.pop()
                answer += 2
                continue
        bag.append(a)
            
    return answer