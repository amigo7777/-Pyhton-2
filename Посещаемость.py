n = int(input())
n1 = n
l, l2, l3 = list(), list(), list()
s = ''
count = 0
while n != 0:
    c = [input() for j in range(int(input()))]
    l.append(c)
    n -= 1
for i in l:
    s += ' '.join(i) + ' '
l2 = s.split(' ')
for i in range(len(l2)):
    for j in range(i+1, len(l2)):
        if l2[i] == l2[j]:
            count += 1
            if count == n1-1:
                l3.append(l2[i])
    count = 0
print(*l3, sep='\n')
