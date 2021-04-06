name = input('Введитае Ваше имя: ')
age = int(input(f'Здравствуйте {name} введите ваш возрост в этом году: '))
year_now = 2021
year_birth = year_now - age
print(f'{name} ваш год рождение {year_birth}')
year_age = int(input(f'{name} введите год чтобы узнать сколько Вам будет лет в этом году: '))
age_input_user = year_age - year_birth
print(f'{name} в {year_age} Вам будет {age_input_user} лет')
