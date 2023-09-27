import prompt
from random import randint


def progression_list(number1):
    item = 0
    progression = []
    counter = 0
    while counter < 10:
        number_listed = number1 + item
        progression.append(number_listed)
        item += number1
        counter += 1
    return progression


def progression_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name ? ')
    print('Hello, ' + name + '!')
    cor_answr_count = 0
    print('What number is missing in the progression?')
    while cor_answr_count < 3:
        number1 = randint(1, 20)
        game_list = progression_list(number1)
        number2 = randint(0, 9)
        answer = game_list.pop(number2)
        game_list.insert(number2, '..')
        question_list = ' '.join(map(str, game_list))
        print(f'Question: {question_list}')
        player_answer = prompt.integer('Your answer: ')
        if player_answer == answer:
            cor_answr_count += 1
            print('Correct!')
        else:
            cor_answr_count = 4
            print(
                f"'{player_answer}' is wrong answer ;(. "
                f"Correct answer was '{answer}'\nLet's "
                f"try again, {name}!")
        if cor_answr_count == 3:
            print(f'Congratulations, {name}!')
