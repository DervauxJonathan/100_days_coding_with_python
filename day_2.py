print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? € "))
pourcentage_tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
bill_with_tip = bill * ( 1 + pourcentage_tip / 100) 

number_people = int(input("How many people to split the bill? "))
price_per_person = bill_with_tip / number_people
final_bill = round(price_per_person, 2)

print(f"Each person should pay: {final_bill}€" )