num = int(input())
for l in range(num):
    k = int(input())
    n = int(input())
    floor = [i for i in range(1,n+1)]
    for cheung in range(0,k):
        for ho in range(1,n):
            floor[ho] += floor[ho-1]
    print(floor[-1])        
