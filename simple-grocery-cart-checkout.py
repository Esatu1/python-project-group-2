## 2. Simple Grocery Cart Checkout
# Write a program that:
# Has a predefined dictionary of groceries with prices.
# Lets the user “add” items by typing their names.
# For each valid item, asks for the quantity.
# Keeps adding to the cart until the user types "checkout".
# Displays a final bill: each item, quantity, subtotal, and total.
# Skills practiced: dictionaries, loops, input(), math operations, formatting, error handling

## Predefined dictionary of grocery items with their prices
groceries = {
    "soda": 2.5,
    "potato": 4.3,
    "Sweet potato": 4.9,
    "onion": 1.5,
    "carrot": 3.4,
    "garlic": 8.0
}

## This will store items added by the user in the format: {item: quantity}
cart = {}

print("Welcome to the Grocery Store!")
print("Type the name of the item to add it to your cart.")
print("Type 'checkout' to finish and see your bill.\n")

# Start the loop to accept items
while True:
    item = input("Enter item name (or 'checkout'): ").lower()

    # Stop loop if user types 'checkout'
    if item == "checkout":
        break

    # Check if the entered item exists in the grocery list
    if item not in groceries:
        print("Item not found. Please choose from the available items.\n")
        continue

    # Ask for quantity of the valid item
    try:
        quantity = int(input(f"How many {item}s would you like? "))
        if quantity <= 0:
            print("Quantity must be at least 1.\n")
            continue
    except ValueError:
        print("Please enter a valid number for quantity.\n")
        continue

    # Add or update the item in the cart
    if item in cart:
        cart[item] += quantity
    else:
        cart[item] = quantity

    print(f"Added {quantity} {item}(s) to your cart.\n")

# === Final Checkout ===
print("\n Final Bill:")
print("-" * 20)

total_cost = 0

for item, quantity in cart.items():
    price = groceries[item]
    subtotal = price * quantity
    total_cost += subtotal
    print(f"{item.title()} x {quantity} = ${subtotal:.2f}")

print("-" * 20)
print(f"Total: ${total_cost:.2f}")
print("Thank you for shopping with us!")
