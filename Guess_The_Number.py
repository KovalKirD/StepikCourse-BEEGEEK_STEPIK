# Угадай Число
import random  # Модуль рандом
def is_valid(num):  # Функция валидации введенного значения пользователем
    return num.isdigit() and 1 <= int(num) <= 100

print('Угадайте число от 1 до 100')
cifra = random.randint(1, 100)  # Загаданное число
num = -1     # Число пользователя
popitki = 1  # Колличество попыток

while num != cifra:  # Пока не угадана cifra
    print('Введите ваше число:')
    num = input()

    if is_valid(num) == False:  # Проверка на дурака
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue

    num = int(num)

    if num > cifra:
        print('Слишком много, попробуйте еще раз')
        popitki += 1
        continue
    elif num < cifra:
        print('Слишком мало, попробуйте еще раз')
        popitki += 1
        continue
    elif num == cifra:
        print('Вы угадали, поздравляем!')
        print('Kоличество попыток:', popitki)

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
# Пустая строка