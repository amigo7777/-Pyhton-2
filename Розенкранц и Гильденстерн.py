s = input()
count = 0
lst = []
for i in s:
    if i == 'о':
        count += 1
    else:
        lst.append(count)
        count = 0
print(max(lst))
