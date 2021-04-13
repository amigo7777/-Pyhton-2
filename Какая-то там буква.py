message = str(input())
number = int(input())
if len(message) >= number >= 1:
    print(message[number-1])
else:
    print('ОШИБКА')
