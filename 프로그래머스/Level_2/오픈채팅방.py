def solution(record):
    answer = []
    new_answer = []
    obj_name = {}
    
    for r in record:
        arr = r.split(' ')
        action = arr[0]
        user = arr[1]
        
        if len(arr) > 2:
            name = arr[2]
            obj_name[user] = name
        
        if action == 'Enter':
            answer.append(user+'/'+'님이 들어왔습니다.')
        elif action == 'Leave':
            answer.append(user+'/'+'님이 나갔습니다.')
            
    for a in answer:
        arr = a.split('/')
        new_answer.append(obj_name[arr[0]]+arr[1])
    
    return new_answer

# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges