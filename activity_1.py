# Define a dictionary of item prices with index numbers as keys
item_price = {
    1: 50,    # Item 1 costs Rs. 50
    2: 100,   # Item 2 costs Rs. 100
    3: 150    # Item 3 costs Rs. 150
}

# Ask the user to enter an index number
# Wrap in try-except to safely handle invalid input
try:
    user_input = int(input("Please enter a number (1, 2, or 3): "))  # Convert input to integer

    # Check if the entered index exists in the dictionary
    if user_input in item_price:
        print(f"✅ Price of item {user_input}: Rs. {item_price[user_input]}")
    else:
        print("❌ Invalid item number. Please enter 1, 2, or 3.")

except ValueError:
    # This runs if user enters something that can't be converted to int
    print("⚠️ Invalid input. Please enter a number like 1, 2, or 3.")