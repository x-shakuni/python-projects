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
import random
random_list = []
for i in range(0,100):
    random_list.append(i+1)
random_choice = random.choice(random_list)
print(random_choice)
condition = True

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
    attempt = 10
else:
    attempt = 5

while condition and attempt > 0:
    print('\n'*1)
    print(f"You have {attempt} attempts left!!")
    user = int(input("Guess the number: "))
    if user == random_choice:
        print("Great, you have guessed the number!")
        condition = False
    elif user > random_choice:
        print("Your guess was too high!")
        print("Guess Again!")
    elif user < random_choice:
        print("Your guess was too low!")
        print("Guess Again!")
    else:
        print("Invalid Input!")

    attempt-=1



if condition == True:
    print(f"Game Over, The number was {random_choice}")
