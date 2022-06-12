"""This is version 2 of the base component for the product value comparison
program.
I have added the string checker that checks if the string inputed is not blank
"""


# Functions go here


# Integer checking function - loops until a valid number is entered
def number_checker(question, output):
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
