gain = int(input('Введите значение выручки'))
costs = int(input('Введите значение издержек'))
profit = gain - costs
if profit > 0:
    profitable = (profit / gain)
    print('Вы в прибыли')
    print(f'Отношение прибыли к выручки {profitable}')
    ammount_staff = int(input('Введите количество персонала в фирме: '))
    profit_ammount_staff = profit / ammount_staff
    print(f'Ваша приболь на одного сотрудника состваляет: {profit_ammount_staff}')
else:
    print('Вы в убытке')
