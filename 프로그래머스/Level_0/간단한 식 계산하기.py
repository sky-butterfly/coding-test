def solution(binomial):
    answer = 0
    
    arr = binomial.split(' ')
    a = int(arr[0])
    op = arr[1]
    b = int(arr[2])
    
    if( op == '+'):
        answer = a+b
    elif(op == '-'):
        answer = a-b
    else:
        answer = a*b
    
    return answer