t = int(input())
for i in range(t):
    num, word= input().split()
    num = int(num)
    new = ''

    for j in range(len(word)):
        for i in range(num):
            new += word[j]
    print(new)
    