trip = {
    "Destination": input("Enter destination: "),
    "Number of days": int(input("Enter number of days: ")),
    "Hotel cost": float(input("Enter hotel cost: ")),
    "Travel cost": float(input("Enter travel cost: ")),
    "Food cost": float(input("Enter food cost: "))
}

total_expense = (
    trip["Hotel cost"]
    + trip["Travel cost"]
    + trip["Food cost"]
)

print("\n--- Trip Details ---")
for key, value in trip.items():
    print(key, ":", value)

print("Total Trip Expense:", total_expense)
