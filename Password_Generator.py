# Генератор Паролей
import random  # Модуль рандом
# Константы:
DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'

def generate_password(length, chars):  # Функция генерации пароля
    pass_gen = ''
    for char in range(length):
        pass_gen += random.choice(chars)
    return pass_gen

chars = ''  # Символы, которые могут быть в генерируемом пароле

count_pass = int(input('Сколько паролей необходимо?'))
length_pass = int(input('Длинна пароля?'))
confirm_num = input('Включать ли цифры 0123456789 ?')
confirm_uppercase = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ ?')
confirm_lowercase = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz ?')
confirm_symbol = input('Включать ли символы !#$%&*+-=?@^_?')
confirm_symbol_ambiguous = input('Исключать ли неоднозначные символы il1Lo0O ?')

# Проверка ответов пользователя
if confirm_num == '+':
    chars += DIGITS
if confirm_uppercase == '+':
    chars += UPPERCASE_LETTERS
if confirm_lowercase == '+':
    chars += LOWERCASE_LETTERS
if confirm_symbol == '+':
    chars += PUNCTUATION
if confirm_symbol_ambiguous == '+':
    for symbol_ambiguous in 'il1Lo0O':
        chars = chars.replace(symbol_ambiguous, '')

# Генерируем пароли в колличестве count_pass
for znach in range(count_pass):
    print(generate_password(length_pass, chars))
# Пустая строка