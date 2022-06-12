"""This is the first version of get product details
this version makes sure the next product the user is comparing is in the same
unit type
"""
# Variables
product_amount = []
product_price = []
loop = 0
set_constant_unit_type = 0
constant_unit_type = ""


# Functions
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
# Basic while loop for testing
while loop <= 1:
    get_product_details()
    loop += 1
print(product_amount, product_price)
