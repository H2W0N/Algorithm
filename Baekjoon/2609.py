# 최대공약수와 최소공배수
m, n = map(int, input().split())
a = []
for i in range(1,min(m,n)+1) :
    if m%i == 0 and n%i == 0:
        a.append(i)

print(max(a))
print(int(m*n/max(a)))

# 다른 사람의 풀이
# 유클리드 호제법
a, b = map(int, input().split())

def gcd(a,b) :
    while b > 0 :
        a, b = b, a%b
        return a
    
def lcm(a,b) :
    return a*b//gcd(a,b)

print(gcd(a,b))
print(lcm(a,b))