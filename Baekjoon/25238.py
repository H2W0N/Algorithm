# 가희와 방어율무시

a, b = input().split()
a = int(a)
b = int(b)
c = a*b/100
d = a - c
if d < 100 :
    print(1)
else :
    print(0)
    
# 다른사람의 풀이
a, b = map(int, input().split())
print(int(a*(100-b)/100<100))