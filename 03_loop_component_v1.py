""" First version of the Loop Component
This keeps asking for user input until they reply N to the continue message
"""
# Variables
loop = True


# -------------Main Routine------------- #
while loop is True:
    valid = False
    string = input("Enter a string: ")
    add_more_product = input("Do you wish to continue"
                             " entering strings? (Y/N) ").lower()
    while add_more_product != "y" and add_more_product != "n":
        add_more_product = input("Please enter Y for Yes or N for No ").lower()
    if add_more_product == "n":
        loop = False
