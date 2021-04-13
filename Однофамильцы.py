lastname = [input() for i in range(int(input()))]
count = 0
for i in range(len(lastname)):
    for j in range(i+1, len(lastname)):
        if lastname[i] == lastname[j]:
            count += 1
if count == 0:
    print(count)
else:
    print(count+1)
