m = int(input())
n = int(input())
a = []
for i in range(m,n+1):
    for x in range(2,i+1):
        if i%x == 0:
            if x == i:
                a.append(x)
            break
            
if len(a) == 0:
    print(-1)
else:
    print(sum(a))
    print(min(a))

