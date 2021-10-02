good_tip = 0.20
fair_tip = 0.15
bad_tip = 0.10
split_number = 0
tip_amount = 0
total = 0
amount_per_person = 0

total_bill_amount = input("Total bill amount?" + " ")
level_of_service = input("Level of service? Good, Fair, or Bad." + " ")
split_number = input("Split how many ways?")

if level_of_service == "Good":
    tip_amount = float(total_bill_amount) * good_tip
    total = float(total_bill_amount) + tip_amount
elif level_of_service == "Fair":
    tip_amount = float(total_bill_amount) * fair_tip
    total = float(total_bill_amount) + tip_amount
elif level_of_service == "Bad":
    tip_amount = float(total_bill_amount) * bad_tip
    total = float(total_bill_amount) + tip_amount
else:
    break

amount_per_person = total/split_number

print("You tipped"  + " $" + str(tip_amount) + " " + "and your total is" + " $" + str(total))
print("Total amount: $")