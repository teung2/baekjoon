x = int(input())
line= 1
while True:
    if x<=sum(range(1,line+1)):
        break
    line+=1
    
line_seq = x-sum(range(1,line))    
if line % 2 == 0:
    a = line_seq
    b = line+1-line_seq      
else:
    a = line+1-line_seq
    b = line_seq
print(f'{a}/{b}')

    