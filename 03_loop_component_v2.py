""" Second version of the Loop Component
Integrated "02_get_product_name_v3" into the loop component
"""
# Variables
loop = True


# Functions

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


# -------------Main Routine------------- #
while loop is True:
    get_product_name("Enter the product name: ")
    add_more_product = input("Do you wish to add compare"
                             " another product? (Y/N) ").lower()
    while add_more_product != "y" and add_more_product != "n":
        add_more_product = input("Please enter Y for Yes or N for No ").lower()
    if add_more_product == "n":
        loop = False

