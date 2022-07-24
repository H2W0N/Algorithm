# 피보나치 수 5

cur, next = 0, 1
for _ in range(int(input())) :
    cur, next = next, cur + next
print(cur)

# 다른 사람의 풀이
def fibo(n) :
    if n<2 :
        return n
    else :
        return fibo(n-1) + fibo(n-2)
print(fibo(int(input())))