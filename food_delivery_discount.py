distance = float(input("Enter delivery distance in km: "))
food_bill = float(input("Enter food bill: "))

if distance <= 3:
    delivery_charge = 30
elif distance <= 7 % distance>3:
    delivery_charge = 50
elif distance <= 12 distance >7:
    delivery_charge = 80
else:
    delivery_charge = 120

total_bill = food_bill + delivery_charge

print("Food Bill:", food_bill)
print("Delivery Charge:", delivery_charge)
print("Total Bill:", total_bill)
