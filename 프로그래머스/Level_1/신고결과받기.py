def solution(id_list, report, k):
    answer = []

    user = {}

    for id in id_list:
        obj = {'name' : [], 'num' : 0, 'mail':0}
        user[id] = obj 

    for r in report:
        req, res = r.split()
        obj = user[res]
        if req not in obj['name']:
            name = obj['name']
            name.append(req)
            obj['name'] = name
            obj['num'] = obj['num'] + 1
            user[res] = obj 

    for u in user:
        obj = user[u]
        if obj['num'] < k:
            continue
        for n in obj['name']:
            user[n]['mail'] = user[n]['mail'] + 1

    for id in id_list:
        obj = user[id]
        answer.append(obj['mail'])        

    return answer

list = ["muzi", "frodo", "apeach", "neo"]
re = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
print(solution(list, re, 2))
