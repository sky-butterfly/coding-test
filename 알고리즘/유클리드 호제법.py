# 최대 공약수를 O(logN) 으로 구할 수 있는 유클리드 호제법
# a, b 의 최대 공약수는 b 와 a%b 의 최대공약수와 같다.

a = 8
b = 12

while a%b != 0:
    a, b = b, a%b 

print(b) # 4