from random import *


def is_valid(num):
    return num.isdigit()


def random_generation(random_right):
    return randint(1, random_right)


def request_input(n):
    while True:
        if is_valid(n):
            my_number = int(n)
            return my_number


def comparison_number():
    print('Введите правую границу для числа')
    random_right = int(input())
    random_number = random_generation(random_right)
    print(random_number)
    counter = 0
    while True:
        print(f'Введите число от 1 до {random_right}')
        number = input()
        my_number = request_input(number)
        counter += 1
        if my_number < 1 or my_number > random_right:
            print(f'Число должно быть от 1 до {random_right}')
            continue
        if my_number > random_number:
            print('Твоё число больше')
        elif my_number < random_number:
            print('Твоё число меньше')
        else:
            return print('Ты победил'), print('Количество попыток:', counter)


def game_guessing_number():
    print('Хочешь сыграть в числовую угадайку?')
    wanted_game = input().lower()
    if wanted_game in (['yes', 'да', 'д', 'l']):
        comparison_number()
        while True:
            print('Сыграем ещё раз?')
            play_again = input().lower()
            if play_again in (['yes', 'да', 'д', 'l']):
                comparison_number()
            else:
                return print('Приходи ещё :(')
    else:
        return print('Пока :(')


game_guessing_number()
print('Commit')
