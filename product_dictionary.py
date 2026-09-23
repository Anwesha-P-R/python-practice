product = {
    "Product name": input("Enter product name: "),
    "Price": float(input("Enter price: ")),
    "Brand": input("Enter brand: "),
    "Quantity": int(input("Enter quantity: "))
}

print("\n--- Keys ---")
for key in product.keys():
    print(key)

print("\n--- Values ---")
for value in product.values():
    print(value)

print("\n--- Keys and Values ---")
for key, value in product.items():
    print(key, ":", value)

total_price = product["Price"] * product["Quantity"]

print("\nTotal Price:", total_price)
