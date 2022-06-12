"""First version of "02_get_product_name"
This function checks if the input is blank or not.
"""


# functions
def get_product_name(question):
    valid = ""
    while not valid:
        response = input(question)
        if not response:
            print("You can't leave this blank")
        else:
            return response


# -------------Main Routine------------- #
get_product_name("Enter the product name: ")