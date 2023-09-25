import prompt
from random import randint
import math


def gcd_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name ? ')
    print('Hello, ' + name + '!')
    cor_answr_count = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while cor_answr_count < 3:
        number1 = randint(1, 50)
        number2 = randint(1, 50)
        print(f'Question: {number1} {number2}')
        join = prompt.integer('Your answer: ')
        cor_gcd = math.gcd(number1, number2)
        if join == cor_gcd:
            cor_answr_count += 1
            print('Correct!')
        else:
            cor_answr_count = 4
            print(
                f"'{join}' is wrong answer ;(. "
                f"Correct answer was '{cor_gcd}'\nLet's "
                f"try again, {name}!")
        if cor_answr_count == 3:
            print(f'Congratulations, {name}!')
