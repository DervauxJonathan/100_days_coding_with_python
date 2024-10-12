import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

move_list = [rock, paper, scissors]

input_player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

if input_player <= 2:
    print(f"You choose: \n {move_list[input_player]}")
else:
    print("")

action_computer = random.randint(0, 2)
print(f"The computer choose: \n {move_list[action_computer]}")

if input_player >= 3 or  input_player < 0:
    print("You Typed an invalid number. You lose")
elif input_player == 0 and action_computer == 2:
    print("You Win")
elif action_computer == 0 and input_player == 2:
    print("You Lose")
elif input_player > action_computer:
    print("You Win")
elif input_player < action_computer:
    print("You Lose")
elif input_player == action_computer:
    print("it's a Draw")