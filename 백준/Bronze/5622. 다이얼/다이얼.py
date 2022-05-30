a = input().lower()
cnt = 0
for i in a:
    if (i == 'a') | (i == 'b') | (i =='c') :
        cnt += 3
    elif (i == 'd') | (i == 'e') | (i =='f') :
        cnt += 4
    elif (i == 'g') | (i == 'h') | (i =='i') :
        cnt += 5
    elif (i == 'j') | (i == 'k') | (i =='l') :
        cnt += 6
    elif (i == 'm') | (i == 'n' )| (i =='o') :
        cnt += 7
    elif (i == 'p') | (i == 'q') | (i =='r') | (i =='s'):
        cnt += 8
    elif (i == 't') | (i == 'u') | (i =='v') :
        cnt += 9
    elif (i == 'w') | (i == 'x') | (i =='y') | (i =='z'):
        cnt += 10
    else:
        cnt += 11
print(cnt)
        
    
    