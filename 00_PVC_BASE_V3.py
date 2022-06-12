"""This is version 3 of the base component for the product value comparison
program.
I have added 03_loop_component_v3 to allow users to compare multiple products
"""


# Functions go here
loop = True
num_of_products = 0


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


# String checking function - checks if the string inputed it blank or not
def get_product_name(question):
    valid = ""
    while not valid:
        response = input(question)
        if not response:
            print("You can't leave this blank")
        elif len(response) <= 3:
            confirm = input("Your response seems to be quite short, are you"
                         " sure this is what you want? (Y/N) ").lower()
            y_or_n = False
            while y_or_n is False:
                if confirm == "y":
                    return response
                elif confirm == "n":
                    y_or_n = True
                else:
                    confirm = input ("Please enter Y for Yes or N for No ")
        else:
            return response


# -------------Main Routine------------- #
# Getting maximum budget
get_max_budget("Enter your maximum budget: ", "Your max budget is: $")

# Loop code for inputting multiple products
while loop is True:

    get_product_name("Enter the product name : ")  # Calling get_product_name
    num_of_products += 1

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
