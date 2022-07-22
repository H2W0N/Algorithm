# 최소, 최대

cnt = int(input())
n = list(map(int, input().split()))
max = n[0];
min = n[0]

for i in n[1:] :
    if i>max :
        max = i
    elif i<min : 
        min = i
print(min, max)

# 다른 사람의 풀이
cnt = int(input())
numbers = list(map(int, input().split()))
print(min(numbers), max(numbers))