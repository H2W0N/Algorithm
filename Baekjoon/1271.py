# 엄청난 부자2

n, m = input().split()
n = int(n)
m = int(m)
a = n//m
print(a)
print(n-a*m)

# 다른 사람의 풀이
n, m = map(int, input().split())
print(n//m) # 몫을 반환
print(n%m) # 나머지를 반환