"""Third version of the number checking function
based on "01_check_max_budget_v2"
I noticed that the integer checker would allow negative numbers, so I updated
it to not allow negative numbers
"""

# Integer checking function - loops until a valid number is entered


def number_checker(question, output):
    error = "\nPlease enter a NUMBER above 0"       # error message
    number = ""
    while not number:
        try:
            number = float(input(question))    # asking for user input
            while number <= 0:      # check that the number is above 0
                print(error)
                number = float(input(question))
            return print(output, round(number, 2))
        except ValueError:
            print(error)


# -------------Main Routine------------- #
number_checker("Enter your maximum budget: ", "Your max budget is: $")
