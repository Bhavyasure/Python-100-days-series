# In this we will be building tip calculator and splitter using input function,
# Different data types, Mathematical Operators these are the topics that are going to cover in this project
#This project is quite easy and simple

print("Welcome to the Tip Calculator!!")
bill=float(input("What was the total bill?$ "))
tip=int(input("How much percentage Tip would you like to give? 10,12,15 "))
people=int(input("How many people want to share the bill?"))
bill_with_tip= bill*(1+tip/100)
bill_per_person=bill_with_tip/people
final_amount=round(bill_per_person,2)
print(f"Each person should pay: ${final_amount}")

