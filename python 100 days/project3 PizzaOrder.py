#Hey welcome back to 100 days of 100 projects todays let's build the pizza delivery
# application with some addons on pizza
#In today's project we are going to cover the topica like
# Conditional Statements,Mathematical Operations, Logical Operations


print("Welcome to Cheezy Wheels Pizzas!!")
size=input("Which size of Pizza would you like to have? S, M or L: ")
extra_cheese=input("Do you want extra cheese? Y or N: ")
pepperoni=input("Do you want pepperoni on your pizza? Y or N: ")
bill=0
if size == "S" or "s":
    bill+=15
elif size=="M" or "m":
    bill+=25
elif size == "L" or "l":
    bill+= 35
else:
    print("Enter the proper input!!")

if pepperoni=="Y" or"y":
    if size=="S" or "s":
        bill+=2
    else:
        bill+=3

if extra_cheese=="Y" or "y":
    bill+=2

print(f"Your final bill will be {bill}.")