import os
import time
import random

print('Welcome to the Math Game!')


def clear_screen():
    os.system('cls')

points = 0
total_time = 0
questions = 0

while True:
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    operator = random.choice(['+', '-'])

    expression = str(num1) + " " + operator + " " + str(num2)
    answer = eval(expression)

    questions += 1

    print('What is the answer to the following expression')
    print(expression, "= ?")

    start_time = time.time()

    while True:
        try:
            user_answer = int(input('Your answer: '))
            break
        except:
            print('Please enter a valid number')


    end_time = time.time()

    elapsed_time = end_time - start_time

    if user_answer == answer:
        print('Correct!')
        points += 1
        total_time += elapsed_time
        time.sleep(1)


        clear_screen()


    else:
        print('Game Over!')
        print('The correct answer was', answer)

        print('You earned', points, 'points!')
        print('You spent', round(total_time, 2), 'seconds playing this game.')
        print('You answered a total of', questions, 'questions.')
        print('Your average time per question was', round((total_time / questions), 2), 'seconds.')
        break