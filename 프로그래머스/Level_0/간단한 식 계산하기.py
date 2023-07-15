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
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges