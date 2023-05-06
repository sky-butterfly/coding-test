def solution(numbers, direction):
    if direction == 'right' :
        tmp = numbers.pop()
        numbers.insert(0, tmp)
        return numbers
    
    tmp = numbers.pop(0)
    numbers.append(tmp)
    return numbers