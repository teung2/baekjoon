num = int(input())
for i in range(num):
    h, w, n = map(int,input().split())
    yy = n%h
    xx = n//h+1
    if yy==0:
        yy = h
        xx = n//h   
    print(yy*100+xx)
