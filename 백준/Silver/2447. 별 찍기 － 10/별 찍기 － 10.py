def star(n):
    if n == 3:
        return ['***','* *','***']
    
    lst = star(n//3)
    stars = []
    
    for i in lst:
        stars.append(i*3)
    for i in lst:
        stars.append(i+' '*(n//3)+i)
    for i in lst:
        stars.append(i*3)
    return stars
n = int(input())
print('\n'.join(star(n)))