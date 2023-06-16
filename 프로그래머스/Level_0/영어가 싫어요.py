def solution(numbers):
    answer = ''
    obj = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    
    word = ''
    for n in numbers:   
        word += n
        
        if (word in obj.keys()) == False:
            continue
        answer += obj[word]
        word = ''
    
    return int(answer)