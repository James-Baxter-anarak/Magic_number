import random
import time

print('Добро пожаловать в числовую угадайку')
quant = random.randint(1, 100)
time.sleep(1.7)
print('Генерирую для вас особое число =)! Попробуйте его отгадать...')
time.sleep(1.5)
print('...')
time.sleep(1.5)
print('...')
time.sleep(1.5)
print('...', 'Итак, поехалиии!', sep='\n')


def function(w=None) -> object:
    total = 0
    def is_valid(s):
        if (s.isdigit() == True) and 1 <= int(s) <= 100:
            return True
        else:
            return False

    while True:
        s = input('Введите целое число от 1 до 100:')
        if not is_valid(s):
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue
        s = int(s)
        if s < quant:
            total += 1
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif s > quant:
            total +=1
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            total +=1
            time.sleep(2.0)
            print('Секундочку, думаю... 0_о')
            time.sleep(1.0)
            print('бииип')
            time.sleep(1.0)
            print('бииип')
            time.sleep(1.0)
            print('бииип')
            time.sleep(2.5)
            print('Не может быть! Вы угадали, поздравляем!')
            print('Попыток было совершенно:', total)  # Попыток было совершенно:
            time.sleep(2.0)
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break
    time.sleep(3.0)
    print('Хотите повторить? (Y/N)')
    if input().upper != 'Y':
        return function()


time.sleep(2.0)
function()
