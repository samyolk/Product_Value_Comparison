"""First version of the number checking function
"""

# Integer checking function - loops until a valid number is entered


def number_checker(question):
    error = "\nSorry, you must enter an integer\n"
    number = ""
    while not number:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print(error)


# -------------Main Routine------------- #
number_checker("Enter budget: ")
