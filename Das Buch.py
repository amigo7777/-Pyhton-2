print('<<< Книги на лето >>>')
l, l2 = list(), list()
count = 0
n, n2 = int(input()), int(input())
for i in range(n):
    s = input()
    l.append(s)
for j in range(n2):
    s2 = input()
    l2.append(s2)
for j in range(n2):
    for i in range(n):
        if l[i] == l2[j]:
            count += 1
    if count == 0:
        print('NO')
    else:
        print('YES')
        count = 0
