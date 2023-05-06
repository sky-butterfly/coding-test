def solution(box, n):
    answer = 0
    a = box[0] * box[1]
    dice = n ** 2
    
    if n > box[1] or n > box[2] or n > box[0] :
        return answer
    
    answer = int(box[0]/n) * int(box[1]/n) * int(box[2]/n)
    
    return answer