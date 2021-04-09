def user_info(name, family, ya_b, city, email, tel):
    return (
        f'Имя: {name} Фамилия: {family} год рождения: {ya_b} город проживания: {city} email: {email} телефон: {tel}')


input_name = input('Введит Имя пользователя: ')
input_family = input('Введит Фамилию пользователя: ')
input_ya_b = int(input('Введит год рождения пользователя: '))
input_city = input('Введит город проживания: ')
input_email = input('Введит email проживания: ')
input_tel = input('Введит телефон проживания: ')

print(
    user_info(name=input_name, family=input_family, ya_b=input_ya_b, city=input_city, email=input_email, tel=input_tel))
