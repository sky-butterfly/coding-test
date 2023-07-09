def solution(s):
    answer = []
    obj = {}
    
    s = s[2:len(s)-2]
    arr = s.split("},{")
    
    for a in arr:
        aa = a.split(',')
        obj[len(aa)] = aa
    
    for i in range(1, len(arr)+1):
        aa = obj[i]
        for a in aa:
            if (int(a) in answer) == False:
                answer.append(int(a))
                break
    
    return answer

# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges