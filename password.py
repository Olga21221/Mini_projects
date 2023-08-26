import random

def valid_date(): # проверяем входящие данные на кооректность
    option_y = ['y', 'д', 'yes', 'да']
    option_n = ['n', 'н', 'no', 'нет']
    while True:
        answer = input()
        if answer.lower() in option_y:
            #print('+')
            return True
        elif answer.lower() in option_n:
            #print('-')
            return False
        else:
            print('Неверный ввод. Повторите: ')
            continue


DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'
chars = ''

quantity =  int(input(('Укажите количество паролей для генерации: ')))
length = int(input(('Укажите длину пароля: ')))
print('Включать ли цифры: ')
if valid_date():
    chars = chars + DIGITS
print('Включать ли прописные буквы : ')
if valid_date():
    chars += UPPERCASE_LETTERS
print('Включать ли строчные буквы : ')
if valid_date():
    chars += LOWERCASE_LETTERS
print('Включать ли символы : ')
if valid_date():
    chars += PUNCTUATION

def generate_password():
    psw = ''
    for i in range(length):
        psw = psw + random.choice(chars)
    return psw

for i in range(quantity):
    print(generate_password())
