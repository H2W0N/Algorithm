# 약수 구하기
p, q = input().split()
p = int(p)
q = int(q)
a = []
for i in range(1,p+1) :
    if p%i == 0 :
        a.append(i)

if q > len(a):
    print(0)
else :
    print(a[q-1])
    
# 다른 사람의 풀이
n, k = map(int, input().split())
res = 0
for i in range(1, n+1) :
    if n%i == 0 :
        k -= 1
        if k == 0 :
            res = i
print(res)
