a = []


for i in range(2,246913):
    for j in range(2, int(i**0.5)+1):
        if i %j == 0:
            break
    else:
        a.append(i)
        
while True:
    n = int(input())
    cnt = 0
    if n == 0:
        break
    else:
        for k in a:
            if (k >= n+1) & (k<=2*n):
                cnt +=1
        print(cnt)
    
        

    