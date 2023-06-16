def solution(arr):
    answer = 0
    index = 0
    newArr = []
    
    while(True):
        
        index += 1
        newArr = []
        
        for a in arr:
            if a >= 50 and a%2 == 0:
                newArr.append(int(a/2))
                continue
            if a < 50 and a%2 == 1:
                newArr.append(a*2 + 1)
                continue
            newArr.append(a)
        
        if newArr == arr:
            answer = index-1
            break
        
        arr = newArr
    
    return answer 