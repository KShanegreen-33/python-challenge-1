# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# Order list to store the customer's order
order_list = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Loop for placing an order
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number and valid
    if menu_category.isdigit():
        menu_category = int(menu_category)
        
        if menu_category in menu_items:
            # Save the menu category name to a variable
            menu_category_name = menu_items[menu_category]
            print(f"You selected {menu_category_name}")

            # Print the items in the selected menu category
            i = 1
            item_menu = menu[menu_category_name]
            menu_items.clear()  # Clear the previous menu items
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in item_menu.items():
                if isinstance(value, dict):
                    # Handle items that have subcategories (like Pizza or Drinks)
                    for sub_key, sub_value in value.items():
                        print(f"{i}      | {key} - {sub_key: <22} | ${sub_value}")
                        menu_items[i] = {"Item name": f"{key} - {sub_key}", "Price": sub_value}
                        i += 1
                else:
                    print(f"{i}      | {key: <24} | ${value}")
                    menu_items[i] = {"Item name": key, "Price": value}
                    i += 1

            # Get the customer's selection
            menu_selection = input("What do you want?: ")

            # Validate if the menu selection is a number and a valid menu item
            if menu_selection.isdigit():
                menu_selection = int(menu_selection)
                if menu_selection in menu_items:
                    # Get item details from the menu_items dictionary
                    item_name = menu_items[menu_selection]["Item name"]
                    price = menu_items[menu_selection]["Price"]

                    # Ask for quantity
                    quantity_input = input(f"How many {item_name} would you like to order? (default is 1 if invalid): ")
                    if quantity_input.isdigit():
                        quantity = int(quantity_input)
                    else:
                        quantity = 1  # Default quantity if input is invalid

                    # Add the item to the order list
                    order_list.append({
                        "Item name": item_name,
                        "Price": price,
                        "Quantity": quantity
                    })
                    print(f"Added {quantity} x {item_name} to your order.")
                else:
                    print(f"Error: {menu_selection} is not a valid menu option.")
            else:
                print("Error: The input is not a valid number.")
        else:
            print(f"Error: {menu_category} is not a valid menu option.")
    else:
        print("Error: You Didn't select a number.")

    # Ask if the customer wants to keep ordering
    keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").strip().lower()
    if keep_ordering != "y":
        place_order = False

# Print out the customer's order
print("\nThis is what we are preparing for you.\n")

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# Print each item in the order list
total_cost = 0
for order in order_list:
    item_name = order["Item name"]
    price = order["Price"]
    quantity = order["Quantity"]

    # Format and print the item name, price, and quantity
    print(f"{quantity} x {item_name:<21} | ${price:5.2f} | {quantity:8}")

    # Calculate the total cost
    total_cost += price * quantity

# Print the total cost of the order
print("--------------------------|--------|----------")
print(f"Total cost: ${total_cost:.2f}")