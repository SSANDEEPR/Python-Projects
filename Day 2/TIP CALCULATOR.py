# TIP CALCULATOR

print("Welcome to the tip calculator")
total_bill = input("What was the total bill?\n")
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15?\n")
split_bill = input("How many people to split the bill?\n")
person_bill = (float(total_bill) + int(tip_percentage)) / int(split_bill)
print(f"Each person should pay:{person_bill}")
