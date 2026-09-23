account_holder = input("Enter account holder name: ")
account_number = int(input("Enter account number: "))
account_type = input("Enter account type: ")
opening_balance = float(input("Enter opening balance: "))
deposit = float(input("Enter deposit amount: "))
withdrawal = float(input("Enter withdrawal amount: "))

final_balance = opening_balance + deposit - withdrawal

print("\n--- Account Details ---")
print("Account Holder:", account_holder)
print("Account Number:", account_number)
print("Account Type:", account_type)
print("Opening Balance:", opening_balance)
print("Deposit:", deposit)
print("Withdrawal:", withdrawal)
print("Final Balance:", final_balance)
