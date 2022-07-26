# 최대공약수와 최소공배수
m, n = map(int, input().split())
a = []
b = []
for i in range(1,max(m,n)+1) :
    if m%i == 0 :
        a.append(i)
    if n%i == 0 :
        b.append(i)
gcd = [i for i in a if i in b]

print(max(gcd))
print(int(m*n/max(gcd)))