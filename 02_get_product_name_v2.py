"""Second version of "02_get_product_name"
Noticed that version 1 let a space get inputted so I used the .isalpha()
function so the user can't just input a space
"""


# functions
def get_product_name(question):
    while True:
        response = input(question)
        if not response.isalpha():
            print("\nYou can't leave this blank")
        else:
            return response


# -------------Main Routine------------- #
get_product_name("Enter the product name: ")
