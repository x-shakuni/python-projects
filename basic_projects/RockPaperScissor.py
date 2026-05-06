'''
        Try this game of:
        Rock, Paper, Scissor
'''


import random

actions = ["""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """,
    """
       _______
    ---'    ____)____
             ______)
            _______)
           _______)
    ---.__________)
    """,
    """
      _______
    ---'   ____)____
            ______)
         __________)
        (____)
    ---.__(___)
    """]

user = int(input(print("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissor")))
computer = random.randint(0,2)


print("---------------------------------------------")
print("Player",actions[user])
print("---------------------------------------------")
print("Computer",actions[computer])



if user == 0:
    if computer == 0:
        print("DRAW😒😒")
    elif computer == 1:
        print("Computer Won😣😣")
    elif computer == 2:
        print("You Won😁😁")

elif user == 1:
    if computer == 0:
        print("You Won😁😁")
    elif computer == 1:
        print("DRAW😒😒")
    elif computer == 2:
        print("Computer Won😣😣")

elif user == 2:
    if computer == 0:
        print("Computer Won😣😣")
    elif computer == 1:
        print("You Won😁😁")
    elif computer == 2:
        print("DRAW😒😒")

else:
    print("🤡🤡You have types an invalid option🤡🤡")