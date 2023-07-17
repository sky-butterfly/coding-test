def solution(cards):
    check = [0] * len(cards)
    g, i, group = 0, 0, []
    
    while check.count(0) > 0:
        if check[i] == 1:
            group.append(g)
            i, g = check.index(0), 0
            continue
            
        g += 1
        check[i] = 1
        i = cards[i]-1
        
    group.append(g)
    group.sort(reverse=True)
    
    if len(group) > 1:
        return group[0] * group[1]
    else:
        return 0
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges