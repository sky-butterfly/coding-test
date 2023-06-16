def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def solution(n, m):
    answer = 0
    
    fac_n = factorial(n)
    fac_m = factorial(m)
    fac_n_m = factorial(n-m)
    
    return int(fac_n / (fac_n_m * fac_m))