from art import logo

alphabet = list("abcdefghijklmnopqrstuvwxyz")
print(logo)

def caesar(text, shift, direction):
    if direction == "decode":
        shift = -shift

    result_text = ""

    for letter in text:
        if letter not in alphabet:
            result_text += letter
        else:
            test = alphabet.index(letter)
            test = (test + shift) % len(alphabet)
            result_text += alphabet[test]

    print(f"This is your {direction}d message: {result_text}.")

finish = False

while not finish:
    direction = ""
    while direction not in ["encode", "decode"]:
        direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    original_text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text, shift, direction)

    next = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if next == "no":
        print("Good Bye.")
        finish = True