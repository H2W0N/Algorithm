# 일곱 난쟁이

n, m = 0, 0
arr = [int(input()) for _ in range(9)]
for i in range(9) :
    for j in range(i+1, 9) :
        if sum(arr) - (arr[i]+arr[j]) == 100 :
            n, m = arr[i], arr[j]
arr.remove(n)
arr.remove(m)
print('\n'.join(map(str, sorted(arr))))
