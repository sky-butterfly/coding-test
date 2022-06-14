# 8 X 8 좌표 평면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수 출력

l = input()
x = ord(l[0]) - ord('a')
y = int(l[1]) - 1

result = 0
arr = [(1,2), (2,1), (-1,-2), (-2,-1), (-1, 2), (-2, 1), (1,-2), (2,-1)]

for a in arr:
    if((x+a[0]) > -1 and (y+a[1]) > -1):
        result = result+1

print(result)