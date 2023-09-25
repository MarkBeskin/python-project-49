from random import randint
import prompt


def is_even(random_num):
    if random_num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def even_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name ? ')
    print('Hello, ' + name + '!')
    cor_answr_count = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while cor_answr_count < 3:
        random_num = randint(1, 100)
        print("Question: " + str(random_num))
        answer = is_even(random_num)
        pl_answer = prompt.string('Your answer: ')
        if pl_answer == answer:
            print('Correct!')
            cor_answr_count += 1
            if cor_answr_count == 3:
                print('Coungratulations, ' + name + '!')
        else:
            print("'" + pl_answer + "' is wrong answer ;(.")
            print("Correct answer was " + "'" + answer + "'.")
            print("Let's try again, " + name + "!")
            break
