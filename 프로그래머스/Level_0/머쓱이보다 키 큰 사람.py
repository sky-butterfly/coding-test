def solution(array, height):
    array.append(height)
    array.sort()
    idx = array.index(height)
    
    return len(array)-1-idx