print("Welcome to the Roller Coaster!")
height = int(input("What is your height in cm? "))
ticket = int(input("You may purchase a ticket, how many would you like? "))
if height >= 120:
    age = int(input("How old are you? "))
    adult = 18
    young = 7
    if age < 18:
        bill = young * ticket
        print(f"Your total is ${bill}.")
    else:
        bill = adult * ticket
        print(f"Your total bill is ${bill}")
else:
    print("We are very sorry, you are not able to purchase a ticket at this time.")

payment = input("How would you like to pay? Cash or Card? ")

if payment == "Card":
    print("Please proceed to the next available kiosk")
else:
    print("We can take care of that for you. Thank you have a great day.")

