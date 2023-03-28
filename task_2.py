'''Создайте модуль с функцией внутри. Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
Функция выводит подсказки “больше” и “меньше”. Если число угадано, возвращается истина, а если попытки исчерпаны - ложь. '''

from random import randint
from sys import argv


def function(min, max=100, n=3):
    NUMBER = randint(min, max)
    for i in range(n):
        guess = int(input('Enter your guess: '))
        if guess < NUMBER:
            print("your guess is too small")
            continue
        elif guess > NUMBER:
            print("your guess is too big")
            continue
        else:
            return True
    return False


if __name__ == "__main__":
    name, *arg = argv
    print(function(*(int(x) for x in arg)))
