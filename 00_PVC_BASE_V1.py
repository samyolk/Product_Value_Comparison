"""This is version 1 of the base component for the product value comparison
program.
I have added the integer checker that asks the user for the budget in this
version.
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