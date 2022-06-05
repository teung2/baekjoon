import sys
n = int(sys.stdin.readline())
factorial = 1
for i in range(n,0,-1):
    factorial *= i
print(factorial)