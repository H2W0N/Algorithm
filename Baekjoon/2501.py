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