# 소수
def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우 
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

m, n = map(int, input().split())
l1 = prime_list(m)
l2 = prime_list(n)
print(l1)
print(l2)
for i in range(len(l1)) :
    l2.remove(l1[i])
print(l2)