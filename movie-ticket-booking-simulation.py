# 4. Movie Ticket Booking Simulation
# Simulate a movie theater booking system that:
# Shows a list of available movie titles, showtimes, and seat prices. # type: ignore
# Asks the user to choose a movie and number of tickets. # type: ignore
# Confirms total price and asks if they want to book another movie. # type: ignore
# Ends when they say “no” and displays total bookings and cost. # type: ignore
# Skills practiced: loops, input, conditionals, calculations, nested dictionaries

# Movie Ticket Booking Simulation
# Movie ticket booking simulation

# Step 1: List of available movies with showtimes and prices
movies = {
    "Historic": {"showtime": "6:00 PM", "price": 30},
    "Dramatic": {"showtime": "4:00 PM", "price": 20},
    "Comedy": {"showtime": "9:00 PM", "price": 18}
}

# Step 2: Variables to store total bookings and total cost
total_tickets = 0
total_cost = 0

# Step 3: Welcome message and loop for booking
print("Welcome to the Movie Ticket Booking System!\n")

while True:
    print("Available Movies:")
    for title, info in movies.items():
        print(f"- {title} at {info['showtime']} - ${info['price']} per ticket")
    
    # Step 4: User selects a movie
    movie_choice = input("\nEnter the name of the movie you want to watch: ").title()
    
    if movie_choice not in movies:
        print("Sorry, that movie is not available. Please choose again.\n")
        continue  # Ask again
    
    # Step 5: Ask for number of tickets
    try:
        num_tickets = int(input(f"How many tickets do you want for {movie_choice}? "))
    except ValueError:
        print("Please enter a valid number.\n")
        continue
    
    if num_tickets <= 0:
        print("Number of tickets must be at least 1.\n")
        continue
    
    # Step 6: Calculate price and update totals
    price_per_ticket = movies[movie_choice]["price"]
    cost = price_per_ticket * num_tickets
    total_tickets += num_tickets
    total_cost += cost
    
    print(f"{num_tickets} ticket(s) for {movie_choice} booked. Total cost: ${cost}\n")
    
    # Step 7: Ask if user wants to book another
    another = input("Do you want to book another movie? (yes/no): ").lower()
    if another == "no":
        break
    print()  # Line break

# Step 8: Final summary
print("\n Booking Summary:")
print(f"Total tickets booked: {total_tickets}")
print(f"Total amount to pay: ${total_cost}")
print("Thank you for using our system!")

