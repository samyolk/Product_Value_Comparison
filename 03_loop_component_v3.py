""" Third version of the Loop Component
I realised that the user could input only 1 product so I made it so the
continue message only appears after they input the second product.
"""
# Variables
loop = True
num_of_products = 0


# Functions

# String checking function - checks if the string inputted it blank or not
def get_product_name(question):
    valid = ""
    while not valid:
        response = input(question)
        if not response:
            print("You can't leave this blank")     # error message
        elif len(response) <= 3:
            # double-checking if the user intended to input a short string
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


# -------------Main Routine------------- #

# Loop code for inputting multiple products
while loop is True:

    get_product_name("Enter the product name: ")   # Calling get_product_name
    num_of_products += 1

    # Checking if the user has inputted at least 2 products
    if num_of_products >= 2:
        # asking user if they want to compare more products
        add_more_product = input("Do you wish to add compare"
                                 " another product? (Y/N)").lower()

        while add_more_product != "y" and add_more_product != "n":
            add_more_product = input("Please enter Y for "
                                     "Yes or N for No ").lower()
        if add_more_product == "n":
            loop = False

