import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

final_pwd = ""

print("Welcome to the PyPassword Generator!")
count_letters = int(input("How many letters would you like in your password?\n"))
count_symbols = int(input("How many symbols would you like? \n"))
count_numbers = int(input("How many numbers would you like? \n"))

#easy version

for letter in range (0, count_letters):
    random_number = random.randint(0, len(letters) - 1)
    final_pwd += (letters[random_number])

for symbol in range (0, count_symbols):
    random_number = random.randint(0, len(symbols) - 1)
    final_pwd += (symbols[random_number])

for number in range (0, count_numbers):
    random_number = random.randint(0, len(numbers) - 1)
    final_pwd += (numbers[random_number])

print(final_pwd)

#hard version

hard_pwd = []

for letter in range (0, count_letters):
    random_number = random.randint(0, len(letters) - 1)
    hard_pwd += (letters[random_number])

for symbol in range (0, count_symbols):
    random_number = random.randint(0, len(symbols) - 1)
    hard_pwd += (symbols[random_number])

for number in range (0, count_numbers):
    random_number = random.randint(0, len(numbers) - 1)
    hard_pwd += (numbers[random_number])

random.shuffle(hard_pwd)

final_hard_pwd = ""

for char in hard_pwd:
  final_hard_pwd += char

print(final_hard_pwd)