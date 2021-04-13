s = str(input())
print(s)
while len(s) != 1 and len(s) != 2:
    n = len(s)
    s = s[1:n-1]
    print(s)
