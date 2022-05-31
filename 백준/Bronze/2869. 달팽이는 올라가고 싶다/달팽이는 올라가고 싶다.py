a,b,v = map(int,input().split())
#부등식 시간초과 뜸
#a*k - b*(k-1)>=v, 따라서, k >= (v-b)/(a-b) 나눗셈은 실수형 따라서 몫으로 정수형

if ((v-b)%(a-b) == 0):
    print((v-b)//(a-b))
else:
    print(((v-b)//(a-b))+1)

    