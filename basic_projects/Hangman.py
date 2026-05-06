print("""
    88                                                                            
    88                                                                            
    88                                                                            
    88,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYb,d8 88,dPYba,,adPYba,  ,adPPYYba,  8b,dPPYba,   
    88P'    "8a ""     `Y8 88P'   `"8a a8"    `Y88 88P'   "88"    "8a ""     `Y8  88P'   `"8a  
    88       88 ,adPPPPP88 88       88 8b       88 88      88      88 ,adPPPPP88  88       88  
    88       88 88,    ,88 88       88 "8a,   ,d88 88      88      88 88,    ,88  88       88  
    88       88 `"8bbdP"Y8 88       88  `"YbbdP"Y8 88      88      88 `"8bbdP"Y8  88       88  
                                        aa,    ,88                                
                                         "Y8bbdP"                                 """)


hangman_stages = ['''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''',]

import random
#import hangman_words
word_list = ["ant", "baboon", "badger", "bat", "bear", "beaver", "camel", "cat", "cobra", "coyote",
          "crow", "deer", "dog", "donkey", "duck", "eagle", "fox", "frog", "goat", "goose", "hawk", "lion",
          "lizard", "llama", "mole", "monkey", "moose", "mouse", "otter", "owl", "panda", "parrot",
          "pigeon", "python", "rabbit", "rat", "rhino", "salmon", "seal", "shark", "sheep",
          "sloth", "snake", "spider", "swan", "tiger", "toad", "turkey", "turtle", "whale",
          "wolf", "wombat", "zebra"]
# chosen_word = random.choice(hangman_words.word_list)
chosen_word = random.choice(word_list)
# print(len(chosen_word))
# print(chosen_word)


game_over = False
correct_letters = []
lives = 6

while not game_over:

    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You have already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)


    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"******It was {chosen_word}! You lost!******")


    if "_" not in display:
        game_over = True
        print("******You win!******")

    print(hangman_stages[lives])
    print(f"--------------------{lives} Lives left--------------------------")
