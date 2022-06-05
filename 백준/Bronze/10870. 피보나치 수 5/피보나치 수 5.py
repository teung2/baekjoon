import sys
n = int(sys.stdin.readline())
fibo = [0,1]
if n == 0:
    print(0)
else:
    for i in range(0,n-1):
        fibo.append(fibo[i]+fibo[i+1])
    print(fibo[-1])