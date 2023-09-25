from random import randint
import prompt


def calc_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name ? ')
    print('Hello, ' + name + '!')
    cor_answr_count = 0
    print('What is the result of the expression?')
    while cor_answr_count < 3:
        random_choice = randint(1, 3)
        random_num1 = randint(20, 40)
        random_num2 = randint(1, 10)
        if random_choice == 1:
            print(f"Question: {random_num1} + {random_num2}")
            quiz_sum = random_num1 + random_num2
        elif random_choice == 2:
            print(f"Question: {random_num1} - {random_num2}")
            quiz_sum = random_num1 - random_num2
        elif random_choice == 3:
            print(f"Question: {random_num1} * {random_num2}")
            quiz_sum = random_num1 * random_num2
        pl_answer = prompt.string('Your answer: ')
        if int(pl_answer) != quiz_sum:
            print(f"'{pl_answer}' is wrong answer ;(.")
            print(f"Correct answer was '{quiz_sum}'.")
            print(f"Let's try again,{name}!")
            break
        else:
            print('Correct!')
            cor_answr_count += 1
            if cor_answr_count == 3:
                print('Coungratulations, ' + name + '!')
