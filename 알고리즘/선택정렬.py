l = [3,5,6,8,9,0,2,1,4,7] 
size = len(l)

for i in range(size):
    index = i 
    for j in range(i, len(l)):
        if l[index] > l[j]:
            index = j

    l[i], l[index] = l[index], l[i]

print(l)