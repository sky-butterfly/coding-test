def solution(arr, idx):
    
    sArr = list(map(str, arr[idx:]))
    arr = (''.join(sArr)).split('01')
    
    if '1' in arr[0]:
        return idx
    
    if len(arr) == 1:
        return -1

    return idx + len(arr[0]) + 1
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges