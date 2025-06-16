# List of item numbers, names, and prices for snacks
item_numbers = ["1", "2", "3", "4", "5"]
item_names = ["Chips", "Chocolate Bar", "Soda", "Water", "Cookies"]
item_prices = [1.50, 2.00, 1.75, 1.25, 2.25]

# Display items
print("Welcome to the Vending Machine!")
print("Available items:")
for i in range(len(item_numbers)):
    print(item_numbers[i] + ": " + item_names[i] + " - $" + str(item_prices[i]))

# Track selected items and total cost
selected_items = []
selected_prices = []
total_cost = 0.0

# User input loop
while True:
    choice = input("Enter item number to select or type 'done' to finish: ")
    
    if choice.lower() == "done":
        break
    found = False
    for i in range(len(item_numbers)):
        if choice == item_numbers[i]:
            selected_items.append(item_names[i])
            selected_prices.append(item_prices[i])
            total_cost += item_prices[i]
            print(item_names[i] + " added to your cart.")
            found = True
            break
    if not found:
        print("Invalid selection. Please try again.")

# Print receipt
print("\n--- Receipt ---")
for i in range(len(selected_items)):
    print(selected_items[i] + " - $" + str(selected_prices[i]))
print("Total: $" + str(round(total_cost, 2)))


