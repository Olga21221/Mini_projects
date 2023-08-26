num = random.randint(1, 100)
print("Добро пожаловать в числовую угадайку")
print(num)

def is_valid(number):  # проверяет что входящие данные - число
    if number.isdigit() and 1 <= int(number) < 100:
        return True
    else:
        return False
print('Введите число от 1 до 100')
def is_valid_num():
    while True:
        number = input()
        if is_valid(number):
            return int(number)
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')

def compare_num():
    number = is_valid_num()
    while True:
        if number < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            number = is_valid_num()
            continue
        elif number > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
            number = is_valid_num()
            continue
        else:
            print('Вы угадали, поздравляем!')
            print("'Спасибо, что играли в числовую угадайку. Еще увидимся...'")
            break

compare_num()