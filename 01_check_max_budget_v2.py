"""Second version of the number checking function
based on "01_check_max_budget_v1"
I made it output the user budget while still making it usable universally and
updated the messages
"""

# Integer checking function - loops until a valid number is entered


def number_checker(question, output):
    error = "\nPlease enter a NUMBER above 0"
    number = ""
    while not number:
        try:
            number = float(input(question))
            return print(output, round(number, 2))
        except ValueError:
            print(error)


# -------------Main Routine------------- #
number_checker("Enter your maximum budget: ", "Your max budget is: $")
