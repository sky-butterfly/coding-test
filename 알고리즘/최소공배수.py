a, b = 10, 20

answer = a * b

for i in range(max(a, b), (a*b)+1) :
    if (i%a == 0) and (i%b == 0):
        answer = i

print(answer) # 200