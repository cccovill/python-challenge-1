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

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered


order_list = [ 
 #   {
 #   "Item name": "string",
 #   "Price": float,
 #   "Quantity": int
 # }, {
 #   "Item name": "string",
 #   "Price": float,
 #   "Quantity": int
 # } 
]
order_line_amounts = []



# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")
    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            menu_items2 = {}
            menu_items3 = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2                        
                        }
                        menu_items2[i] =  key2 + " - " + key
                        menu_items3[i] = value2
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    menu_items2[i] = key
                    menu_items3[i] = value
                    i += 1
            # 2. Ask customer to input menu item number
            selected_item = input("Type item number: ")

            # 3. Check if the customer typed a number
            if selected_item.isdigit():
                # Convert the menu selection to an integer
                item = (int(selected_item))
                # 4. Check if the menu selection is in the menu items
                if item in menu_items2.keys():
                    # Store the item name as a variable
                    menu_item_name = menu_items2[item]
                    menu_item_price = menu_items3[item]
                    # Ask the customer for the quantity of the menu item
                    quantity = input(f"How many {menu_item_name}'s would you like to order? Default = 1.....")
                    order_list.append({
                        "Item name": menu_item_name,
                        "Price": menu_item_price,
                        "Quantity": quantity
                    })
                    # Check if the quantity is a number, default to 1 if not
                    if quantity.isdigit():
                    # Add the item name, price, and quantity to the order list
                        print(" ")
                    # Great, quantity is acceptable and is already in the list                    
                    #
                    else: 
                        # Replace the bogus quantity stored in the order list
                        for item_added in order_list:
                            if menu_item_name == item_added["Item name"] and item_added["Quantity"] == quantity:
                                item_added["Quantity"] = int(1)
                                # print(f'Item {item_added["Item name"]} quantity updated')                                      
                                

                    # Tell the customer that their input isn't valid
                else: 
                    print(f"Item number {item} entered is invalid.")        
            else:
                print("You didn't select a number.")

                # Tell the customer they didn't select a menu option              
        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")
        

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input
        match keep_ordering.lower():
            case 'y':
                # Keep ordering
                place_order = True
                # Exit the keep ordering question loop
                break
            case 'n':
                # Complete the order
                place_order = False        
                # Since the customer decided to stop ordering, thank them for
                # their order
                print("Order complete! Thanks for ordering.")
                # Exit the keep ordering question loop
                break
            case _:           
                # Tell the customer to try again
                print("Unrecognized response.  Please try again.")


# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order

print(order_list)
print (" ")
print("Item name                 | Price  | Quantity   Line Total")
print("--------------------------|--------|----------|-----------")   

# 6. Loop through the items in the customer's order

for order_item in order_list:

    # 7. Store the dictionary items as variables
    menu_item_name = order_item["Item name"]
    menu_item_price = order_item["Price"]
    menu_item_quantity = order_item["Quantity"]
    menu_item_totl = float(menu_item_price) *  int(menu_item_quantity)
    order_line_amounts.append(menu_item_totl)
    

    # 8. Calculate the number of spaces for formatted printing
    num_item_spaces = 24 - len(order_item["Item name"])
    num_item_spaces2 = 7 - len(str(order_item["Price"]))
    num_item_spaces3 = 10 - len(str(menu_item_quantity))
    num_item_spaces4 = 10 - len(str(menu_item_totl)) 
    if (num_item_spaces4) < 0:
        num_item_spaces4 = 6
    # 9. Create space strings
    item_spaces = " " * num_item_spaces
    item_spaces2 = " " * num_item_spaces2
    item_spaces3 = " " * num_item_spaces3
    if int(menu_item_quantity) > 9:
        num_item_spaces4 -= 1    
    item_spaces4 = " " * num_item_spaces4
  

    # 10. Print the item name, price, and quantity
    print(f"{menu_item_name}{item_spaces}  |{item_spaces2}${menu_item_price}|{item_spaces3}{menu_item_quantity}|{item_spaces4}${menu_item_totl:.2f}")
    
# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.

order_sum = sum(order_line_amounts)

print("--------------------------|--------|----------|-----------")
#      1234567890123456789012345678901234567890123456789012345678
num_item_spaces = 23 - len(str(order_sum))
item_spaces = " " * num_item_spaces
print(f"The total amount for your order is{item_spaces}${order_sum:.2f}")