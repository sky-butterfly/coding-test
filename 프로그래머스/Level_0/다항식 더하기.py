def solution(polynomial):
    answer = ''
    
    arr = polynomial.split(' ')
    x_sum = 0
    n_sum = 0
    
    for a in arr:
        if a == '+':
            continue
        if 'x' in a :
            if a == 'x':
                x_sum += 1
            else:
                x_sum += int(a[:len(a)-1])
            continue
        n_sum += int(a)
        
    if x_sum != 0:
        if x_sum == 1:
            answer += 'x'
        else:  
            answer += ( str(x_sum) + 'x' )
    if n_sum != 0:
        if answer != '':
            answer += ' + '
        answer += str(n_sum)
    
    return answer
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges