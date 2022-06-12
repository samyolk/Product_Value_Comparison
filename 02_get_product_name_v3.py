"""Third version of "02_get_product_name"
This function is based on version 1 but it asks the user to confirm if the
inputted value is 3 characters long or under
"""


# functions


# String checking function - checks if the string inputed it blank or not
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
                    confirm = input ("Please enter Y for Yes or N for No ")
        else:
            return response


# -------------Main Routine------------- #
get_product_name("Enter the product name: ")