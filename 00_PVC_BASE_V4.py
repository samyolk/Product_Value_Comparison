"""This is version 3 of the base component for the product value comparison
program.
I have added 03_loop_component_v3 to allow users to compare multiple products
"""


# Variables go here
loop = True
num_of_products = 0
product_amount = []
product_price = []
set_constant_unit_type = 0
constant_unit_type = ""


# Functions go here
# Integer checking function - loops until a valid number is entered
def get_max_budget(question, output):
    error = "\nPlease enter a NUMBER above 0"
    number = ""
    while not number:
        try:
            number = float(input(question))
            while number < 0:
                print(error)
                number = float(input(question))
            return print(output, round(number, 2))
        except ValueError:
            print(error)


# String checking function - checks if the string inputted it blank or not
def get_product_name(question):
    valid = ""
    while not valid:
        response = input(question)
        if not response:
            print("You can't leave this blank")
        elif len(response) <= 3:
            confirm = input("Your response seems to be quite short, are you "
                            "sure this is what you want? (Y/N) ").lower()
            y_or_n = False
            while y_or_n is False:
                if confirm == "y":
                    return response
                elif confirm == "n":
                    y_or_n = True
                else:
                    confirm = input("Please enter Y for Yes or N for No ")
        else:
            return response


# Function to get product price and amount
def get_product_details():
    error = "\nPlease enter a NUMBER above 0"  # error message
    number = ""
    while not number:
        try:
            number = float(input(f"Enter the product price: $"))
            while number <= 0:  # check that the number is above 0
                print(error)
                number = float(input(f"Enter the product price: $"))
            product_price.append(round(number, 2))
        except ValueError:
            print(error)
    unit_type = ""
    conversion_rate = 0
    product_unit = input("Enter the abbreviated unit of measure"
                         " (g, KG, mL or L)").lower()
    while product_unit != "g" and product_unit != "kg" \
            and product_unit != "ml" and product_unit != "l":
        product_unit = input("Please input a valid unit of measure"
                             " (g, KG, mL or L)").lower()
    if product_unit == "g":
        unit_type = "weight"
        conversion_rate = 1
    elif product_unit == "kg":
        unit_type = "weight"
        conversion_rate = 1000
    elif product_unit == "ml":
        unit_type = "volume"
        conversion_rate = 1
    elif product_unit == "l":
        unit_type = "volume"
        conversion_rate = 1000

    # Making sure the constant unit type gets set only once
    global set_constant_unit_type
    global constant_unit_type
    if set_constant_unit_type == 0:
        constant_unit_type = unit_type
        set_constant_unit_type += 1
    while constant_unit_type != unit_type:
        product_unit = input("That is not the same unit type of the product"
                             " you are comparing to. Please enter a "
                             "valid unit type. ").lower()
        if product_unit == "g":
            unit_type = "weight"
            conversion_rate = 1
        elif product_unit == "kg":
            unit_type = "weight"
            conversion_rate = 1000
        elif product_unit == "ml":
            unit_type = "volume"
            conversion_rate = 1
        elif product_unit == "l":
            unit_type = "volume"
            conversion_rate = 1000

    number = ""
    while not number:
        try:
            number = float(input(f"Enter the {unit_type} of"
                                 f" the product: "))  # asking for the amount
            while number <= 0:  # check that the number is above 0
                print(error)
                number = float(input(f"Enter the {unit_type} of "
                                     f"the product: "))
            product_amount.append(round(number * conversion_rate, 2))
        except ValueError:
            print(error)


# -------------Main Routine------------- #
# Getting maximum budget
get_max_budget("Enter your maximum budget: ", "Your max budget is: $")

# Loop code for inputting multiple products
while loop is True:

    get_product_name("Enter the product name : ")  # Calling get_product_name
    num_of_products += 1
    # calling the get product details function
    get_product_details()

    # Checking if the user has inputted at least 2 products
    if num_of_products >= 2:
        # asking user if they want to compare more products
        add_more_product = input("Do you wish to add compare"
                                 " another product? (Y/N)").lower()

        while add_more_product != "y" and add_more_product != "n":
            add_more_product = input("Please enter Y for Yes"
                                     " or N for No ").lower
        if add_more_product == "n":
            loop = False
