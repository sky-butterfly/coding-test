def solution(my_string):
    ord_arr = []
    answer = []
    
    lower_string = my_string.lower()
    
    for ls in lower_string:
        ord_arr.append(ord(ls))
    
    ord_arr.sort()
    
    for oa in ord_arr:
        answer.append(chr(oa))
    
    return ''.join(answer)