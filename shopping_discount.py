amount = int(input("Enter shopping amount: "))

if amount >= 5000:
    discount = amount * 20 / 100
elif amount >= 3000 & amount<5000:
    discount = amount * 15 / 100
elif amount >= 1000 & amount<3000:
    discount = amount * 10 / 100
else:
    discount = 0

final_amount = amount - discount

print("Shopping Amount:", amount)
print("Discount:", discount)
print("Final Amount:", final_amount)
