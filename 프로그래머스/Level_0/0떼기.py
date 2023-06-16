def solution(n_str):
    
    for n in n_str :
        if n.startswith('0'):
            n_str = n_str[1:]
        else :
            return n_str
    
    return n_str