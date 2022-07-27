# N번째 큰 수

T = int(input())
for _ in range(T) :
   arr = list(map(int,input().split()))
   res = sorted(arr)
   print(res[-3])