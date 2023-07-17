def solution(picks, minerals):
    answer = 0
    answer_obj = {0 : {
              'diamond' : 1,
              'iron' : 1,
              'stone' : 1
          },
          1 : {
              'diamond' : 5,
              'iron' : 1,
              'stone' : 1
          },
          
          2 : {
              'diamond' : 25,
              'iron' : 5,
              'stone' : 1
          }}
    
    p_arr = []
    for i, p in enumerate(picks):
        a = [i] * p
        p_arr.extend(a)
    p_arr.sort()
    
    if len(p_arr)*5 < len(minerals):
        minerals = minerals[:len(p_arr)*5]
    
    obj = {}
    m_arr = []
    a = 0
    j = 0
    for i, m in enumerate(minerals):        
        if m == 'diamond':
            a += 10000
        elif m == 'iron':
            a += 60
        else:
            a += 1
        m_arr.append(m)
        
        if i%5 == 4:
            temp = obj.get(a, [])
            temp.append(m_arr)
            obj[a] = temp
            
            a = 0
            m_arr = []
        j += 1
    
    if a > 0 :
        temp = obj.get(a, [])
        temp.append(m_arr)
        obj[a] = temp
    
    i = 0
    keys = sorted(obj, reverse=True)
    for k in keys:
        arr = obj[k]
        for a in arr:
            if i == len(p_arr):
                break
            p = p_arr[i]
            for aa in a:
                answer += answer_obj[p][aa]
            
            i += 1
        
        if i == len(p_arr):
            break
    
    return answer
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges