total = 0

for i in range(1, 8):
    expense = float(input("Enter expense for day " + str(i) + ": "))
    total = total + expense

print("Total Weekly Expense =", total)
