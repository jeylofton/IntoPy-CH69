from catalog import store_items

cart = []

# Helper Function
# Store Name and Menu

def header(text):
    print("------------------------------")
    print(text)
    print("------------------------------")

def menu():
    print("Menu")
    print(" 1. View Catalog")
    print(" 2. Search Produt")
    print(" 3. View Cart")
    # Add more features
    print(" Q. - Quit")

# Catalog and Cart Functions
def print_catalog():
    header("- Our Catalog -")
    for prod in store_items:
        print(f'| {prod["id"]} | {prod["title"].ljust(15)} | {prod["price"]:.2f}')

    answer = input("Type ID to add (N to close): ")
    if answer.lower() == "n":
        return
    else: 
        add_product_to_cart(answer)

def add_product_to_cart(prod_id):
    found = False
    for prod in store_items:
        if str(prod["id"]) == str(prod_id):
            found = True
            cart.append(prod)
            print(f'{prod["title"]} added to your cart.')
            break

def search_product():
    text = input("Search product by title: ").lower()
    found = False
    for prod in store_items:
        if text in prod["title"].lower():
            found = True
            print(f'| {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f}')
            choice = input("Do you want to add this item to your cart? (y/n): ")
            if choice.lower() == "y":
                add_product_to_cart(prod["id"])
            break # stop after first match and added to the cart

    if not found:
        print("Sorry, this item dosent exist")

    def view_cart():
        header("Your Cart")
    if not cart:
        print("Your cart is empty.")
    else:
        for prod in cart:
            print(f'| {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f}')

# Main Program Loop
option = ""
while option != "q" and option != "Q":
    header("Welcome to Store name")
    menu()

    option = input("choose a menu options: ")

    if option == "1":
        print("Viewing the catalog")
    elif option == "2":
        print("Searching Products")
    elif option == "3":
        print("Viewing Cart")
    elif option == "Q" or option == "q":
        print("Thank you for Shopping")
        break
    else:
        print("** ERROR: Invalid Options")
        print("-----------------------/n")