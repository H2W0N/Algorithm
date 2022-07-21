# 이진수
T = int(input())

while T!=0 :
    n = int(input())
    res = []
    while n > 0 :
        if n % 2 == 1 :
            res.append(1)
        else :
            res.append(0)
        n = n // 2 
    
    for i in range(len(res)) :
        if res[i] == 1 :
            print(i, end = " ")
    print()
    T -= 1
    


# 다른 사람의 풀이
T = int(input())
for _ in range(T) :
    n = bin(int(input()))[2:]
    for i in range(len(n)) :
        if n[-i-1] == '1' :
            print(i, end = " ")