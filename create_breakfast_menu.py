#Takes user input for the breakfast menu foods and prices.

customer_name = input("Greetings! Please enter your name. ")
print(f"Welcome, {customer_name}! What would you like to put on the breakfast menu today? ")

def breakfast(menu_breakfast = {}):
    """Starts with an empty dictionary, and takes user input for food as key and
     user input for price as value to create a breakfast menu dictionary."""

    while True:
        food = input(f"Enter a meal option. ")
        price = input(f"Enter the price for {food.title()}. ")
        menu_breakfast[food] = price #User input fills the dictionary.
        add_breakfast = input("Would you like to add more meal options to the breakfast menu? ")
        while not (add_breakfast.lower() == "yes" or add_breakfast.lower() == "no"):
            print("Please enter yes or no.")
            add_breakfast = input("Would you like to add more meal options to the breakfast menu? ")
        if add_breakfast.lower() == 'yes':
            continue
        elif add_breakfast.lower() == 'no':
            break    
    
    print("\nThe breakfast menu is:\n")
    for food, price in menu_breakfast.items():
       print(f"{food.title()} ${price}")
        


menu_breakfast = {}
breakfast(menu_breakfast)



