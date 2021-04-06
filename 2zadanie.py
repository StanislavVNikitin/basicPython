input_user_secunds = int(input('Введите время в секундах: '))
sec = int(input_user_secunds % 60)
h = int(input_user_secunds // 3600)
if h > 0:
    min = int((input_user_secunds % 3600) // 60)
else:
    min = int(input_user_secunds // 60)
if sec < 10:
    sec = '0' + str(sec)
else:
    sec = str(sec)
if min < 10:
    min = '0' + str(min)
else:
    min = str(min)
if h < 10:
    h = '0' + str(h)
else:
    h = str(h)
print(f'Время в формате hh:mm:ss {h}:{min}:{sec}')
