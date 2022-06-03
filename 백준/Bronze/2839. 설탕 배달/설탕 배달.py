sugar = int(input())
bag = 0

while sugar >= 0:
    if sugar%5 == 0:
        print(sugar//5 + bag)
        break
    sugar -= 3
    bag += 1
else:
    print(-1)
