import random
from day_7_word_list import word_list

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''','''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

chosen_word = random.choice(word_list)

placeholder = ""
for position in chosen_word:
    placeholder += "_"
print(placeholder)

state_of_the_game = False
correct_word = []
used_letter = []
lives = 6

while not state_of_the_game:

    display = ""
    print(f"You have currently {lives} lives.")
    if len(used_letter) >= 1:
        print(f"You used those letters {', '.join(used_letter)}.")
    guess = input("Guess a letter: ").lower()
    
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_word.append(guess)
        elif letter in correct_word:
            display += letter
        else:
            display += "_"

    if guess not in chosen_word:
        used_letter.append(guess)
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            state_of_the_game = True
            print("Game Over.")
    
    if lives >=2:
        print(f"You have {lives} lives left.")
    else:
        print(f"You have {lives} live left.")
    print(display)

    if "_" not in display:
        print("You Win")

    print(stages[lives])