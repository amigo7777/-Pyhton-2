s = input()
n = int(input())
s2 = input()
if 0 <= n <= len(s) and len(s2) == 1:
    if s[n-1] == s2:
        print('ДА')
    else:
        print('НЕТ')
else:
    print('ОШИБКА!')
