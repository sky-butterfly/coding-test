def solution(arrayA, arrayB):
    answer = 0
    
    gcd = getGcd(arrayA, answer)    
    if gcd > 1 and getB(arrayB, gcd) == 0:
            answer = gcd
    
    gcd = getGcd(arrayB, answer)    
    if gcd > 1 and getB(arrayA, gcd) == 0:
            answer = gcd
    
    return answer

def getGcd(arr, limit):

    result = arr[0]
    
    for i in range(len(arr)):
        
        a, b = result, arr[i]
        
        while a % b != 0:
            a, b = b, a%b
        
        result = b
    
    if limit != 0 and result < limit:
        result = 1
    
    return result 

def getB(arr, mx):
    result = 0
    
    for a in arr:
        if a%mx == 0:
            result = 1
            break
    
    return result
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges