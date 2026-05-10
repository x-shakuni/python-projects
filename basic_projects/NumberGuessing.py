print("""
:'######:::'##::::'##:'########::'######:::'######:::::::::::'########:'##::::'##:'########::::::::::'##::: ##:'##::::'##:'##::::'##:'########::'########:'########::
'##... ##:: ##:::: ##: ##.....::'##... ##:'##... ##::::::::::... ##..:: ##:::: ##: ##.....::::::::::: ###:: ##: ##:::: ##: ###::'###: ##.... ##: ##.....:: ##.... ##:
 ##:::..::: ##:::: ##: ##::::::: ##:::..:: ##:::..:::::::::::::: ##:::: ##:::: ##: ##:::::::::::::::: ####: ##: ##:::: ##: ####'####: ##:::: ##: ##::::::: ##:::: ##:
 ##::'####: ##:::: ##: ######:::. ######::. ######:::::::::::::: ##:::: #########: ######:::::::::::: ## ## ##: ##:::: ##: ## ### ##: ########:: ######::: ########::
 ##::: ##:: ##:::: ##: ##...:::::..... ##::..... ##::::::::::::: ##:::: ##.... ##: ##...::::::::::::: ##. ####: ##:::: ##: ##. #: ##: ##.... ##: ##...:::: ##.. ##:::
 ##::: ##:: ##:::: ##: ##:::::::'##::: ##:'##::: ##::::::::::::: ##:::: ##:::: ##: ##:::::::::::::::: ##:. ###: ##:::: ##: ##:.:: ##: ##:::: ##: ##::::::: ##::. ##::
. ######:::. #######:: ########:. ######::. ######:::::::::::::: ##:::: ##:::: ##: ########:::::::::: ##::. ##:. #######:: ##:::: ##: ########:: ########: ##:::. ##:
:......:::::.......:::........:::......::::......:::::::::::::::..:::::..:::::..::........:::::::::::..::::..:::.......:::..:::::..::........:::........::..:::::..::
""")

# import random
# random_list = []
# for i in range(0,100):
#     random_list.append(i+1)
# random_choice = random.choice(random_list)
# print(random_choice)
# condition = True
#
# print("Welcome to the Number Guessing Game!")
# print("I am thinking of a number between 1 and 100.")
# difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
#
# if difficulty == 'easy':
#     attempt = 10
# else:
#     attempt = 5
#
# while condition and attempt > 0:
#     print('\n'*1)
#     print(f"You have {attempt} attempts left!!")
#     user = int(input("Guess the number: "))
#     if user == random_choice:
#         print("Great, you have guessed the number!")
#         condition = False
#     elif user > random_choice:
#         print("Your guess was too high!")
#         print("Guess Again!")
#     elif user < random_choice:
#         print("Your guess was too low!")
#         print("Guess Again!")
#     else:
#         print("Invalid Input!")
#
#     attempt-=1
#
#
#
# if condition == True:
#     print(f"Game Over, The number was {random_choice}")
#
###################################################################################################

"""--------------------------Optimized Code--------------------------"""

# Function to check user's guess against actual answer
def check_answer(user_guess, actual_number):
    if user_guess == actual_number:
        print("Great, you have guessed the number!")
    elif user_guess > actual_number:
        print("Your guess was too high!")
    elif user_guess < actual_number:
        print("Your guess was too low!")
    else:
        print("Invalid Input!")

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return 10
    else:
        return 5

from random import randint

def game():
    # Choosing a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    answer = randint(1,100)

    turn = set_difficulty()
    print(f"You have {turn} attempts remaining to guess the number")

    guess = 0
    while guess != answer:
        # Let the user guess a number
        guess = int(input("Make a guess: "))
        check_answer(guess, answer)
        if turn == 0:
            print("You,ve run out of guesses, you loose.")
            return
        elif guess != answer:
            print("Guess Again!")

game()