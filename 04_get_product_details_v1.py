"""This is the first version of get product details
this version reuses the number checker from 01_check_max_budget_v3
"""
# Variables
product_amount = []
product_price = []
loop = 0


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

    while product_unit != "g" and product_unit != "kg"\
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

    number = ""
    while not number:
        try:
            number = float(input(f"Enter the {unit_type} of"
                                 f" the product: "))  # asking for the amount
            while number <= 0:  # check that the number is above 0
                print(error)
                number = float(input(f"Enter the {unit_type} of"
                                 f" the product: "))
            product_amount.append(round(number * conversion_rate, 2))
        except ValueError:
            print(error)


# -------------Main Routine------------- #
get_product_details()
print(product_amount, product_price)
