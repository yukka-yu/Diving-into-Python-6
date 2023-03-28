# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код,
# решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам
# дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для
# случайной расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и
# выведите 4 успешных расстановки.

from random import randint
__all__ = ['queen_check']
string_li = ['17', '24', '32', '48', '56', '61', '73', '85']
N = 8


def queen_check(string_list: [str]) -> bool:
    x = []
    y = []
    flag = True
    for i in range(N):
        x.append(int(string_list[i][0]))
        y.append(int(string_list[i][1]))

    for i in range(N):
        for j in range(i + 1, N):
            if abs(x[i] - x[j]) == abs(y[i] - y[j]):
                flag = False

    return flag


def random_generator_number() -> list[str]:
    list_ = []
    list_x = []
    list_y = []
    while len(list_) < N:
        num = randint(11, 88)
        x = num // 10
        y = num % 10

        if str(num) not in list_ and y != 0 and y != 9 and x not in list_x and y not in list_y:
            list_x.append(num // 10)
            list_y.append(num % 10)
            list_.append(str(num))
    return list_


if __name__ == "__main__":
    # print(queen_check(random_generator_number()))

    # print(random_generator_number())

    count = 0
    print('Ферзи, стоящие на этих позициях, не бьют друг друга:')
    while count < 4:
        b = random_generator_number()
        a = queen_check(b)
        if a:
            print([f'{int(b[i]) // 10} {int(b[i]) % 10}' for i in range(N)])
            count += 1
            