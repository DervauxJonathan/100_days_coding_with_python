from art import logo
import os

print(logo)
print("Welcome to the secret auction program.")

finish = False
bid_list = {}

def bidding_process(bid_list):
    highest_bid = 0
    winner = "" 
    for bidder in bid_list:
        bid_amount = bid_list[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not finish:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bid_list[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()

    if other_bidders not in ["yes", "no"]:
        other_bidders = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    elif other_bidders == "yes":
        os.system('cls')
    elif other_bidders == "no":
        finish = True
        bidding_process(bid_list)

