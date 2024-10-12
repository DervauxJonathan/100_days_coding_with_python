print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
first_path = input("You're at a crossroad, where do you want to go? 'Type 'left' or 'right' ?\n ").lower()

if first_path == "left":
    swim_wait = input("You've come to a lake. There is an island in the middle of the lake. Type 'swim' to swim across. or 'wait' to wait for a boat.?\n").lower()
    if swim_wait == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if door == "yellow":
            print("You found the treasure. You Win!")
        elif door == "red":
            print("It's a room full of fire. Game Over")
        elif door == "blue":
            print("You enter a room of beasts. Game Over")
        else:
            print("You choose a door that doesn't exist. Game Over.")
    else: 
        print("You got attacked by an angry trout. Game Over.")       
else:
    print("You fell in to a hole. Game Over.")
