balance = int(input("Enter account balance: "))
withdrawal = int(input("Enter withdrawal amount: "))

if withdrawal % 100 != 0:
    print("Transaction unsuccessful: Amount must be a multiple of ₹100.")
elif withdrawal > 20000:
    print("Transaction unsuccessful: Maximum withdrawal is ₹20,000.")
elif withdrawal > balance:
    print("Transaction unsuccessful: Insufficient balance.")
else:
    balance_remaining = balance - withdrawal
    print("Transaction successful.")
    print("Remaining Balance:", balance_remaining)
