def solution(my_string):
    answer = ''
    
    arr = ['a', 'e', 'i', 'o', 'u']
    
    for str in my_string:
        if( str in arr ) is False:
            answer += str
    
    return answer