word = input().upper()
unique = list(set(word)) #문자열 중복값 제거 
cnt_lst = []

for i in unique:
    cnt = word.count(i)
    cnt_lst.append(cnt)
 
if cnt_lst.count(max(cnt_lst)) >= 2:
    print('?')
else:
    max_index = cnt_lst.index(max(cnt_lst))
    print(unique[max_index])
    