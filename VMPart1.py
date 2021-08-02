# Author: Kuan Jun Hao Jason
# Admin No: 201484K

def enterInt(prompt, error):
    # for integer data type validation check for customer's input type
    continueLoop = True
    while continueLoop:
        try:
            thevalue = int(input(prompt))
            if thevalue >= 0:
                return thevalue  # return the value if it is a int data type and is more than 0
            else:
                print(error)
        except:
            print(error)  # prints out the error message defined in the function's 2nd argument

drinksDict = {
    'IM': 1.5,
    "HM": 1.2,
    "IC": 1.5,
    "HC": 1.2,
    "1P": 1.1,
    "CC": 1.3
}

# for printing the drinkMenu for the customer
drinkMenu = '''Welcome to ABC Vending Machine.
Select from following choices to continue:
IM. Iced Milo (S$1.50)
HM. Hot Milo (S$1.20)
IC. Iced Coffee (S$1.50)
HC. Hot Coffee (S$1.20)
1P. 100 Plus (S$1.10)
CC. Coca Cola (S$1.30)
0. Exit / Payment
'''

# for printing the vendorMenu for the vendor
vendorMenu = """Welcome to ABC Vending Machine.
Select from following choices to continue:
1. Add Drink Type
2. Replenish Drink
0. Exit
"""

loop = True  # Will remain true forever when the program is running

while loop:
    question = input("Are you a vendor (Y/N)?: ").upper()  # asks the user if he/she is a vendor or a customer
    userstatus = True
    while userstatus:
        if question == "N":  # indicates that the user is not a vendor but a customer
            cancelPurchase = "N"
            print(drinkMenu)  # prints the drink menu for the customer
            choice = ""  # to reset the choice to an empty string for the main while loop below, "while choice != "0":"
            totalPrice = 0  # to reset the total number of drinks selected
            userQuantity = 0  # to reset the total number of selected drinks
            totalAmt = 0  # to reset the amount of money paid by the customer
            while choice != "0":
                userChoice = input("Enter choice: ").upper()
                if userChoice in drinksDict:
                    userQuantity += 1  # add to the total number of selected drinks
                    print("No. of drinks selected =", userQuantity)
                    totalPrice += drinksDict[userChoice]  # adds the price of the drink to the total amount of money that the customer has to pay
                elif userChoice == "0":
                    choice = "0"  # while condition will become false and stops
                else:
                    print("Your selected choice is not in the list.")  # prints a error message if user inputs an invalid id
            if totalPrice == 0:
                print("Thank you and have a nice day!")
                break  # breaks out of the loop if customer did not buy anything or if the customer wants to exit to the "Are you a vendor..." question
            while cancelPurchase != "Y":
                print("\n\nPlease pay: $%.2f\nIndicate your payment:" % totalPrice)
                if cancelPurchase == "N":
                    tenInput = enterInt("Enter no. of $10 notes: ", "Error, please enter a valid number.")  # calling to function to validate customer's input with two arguments instead of crashing the program
                    totalAmt += tenInput*10
                    if totalAmt >= totalPrice:  # checks if the user has paid the sufficient amount
                        userChange = totalAmt - totalPrice
                        if userChange > 0:  # checking if there any change for the customer to take, if there is $0 in change, it will not display the message below
                            print("Please collect your change: $%.2f" % userChange)
                        print("Drinks paid. Thank you.\n\n")
                        userstatus = False  # make condition false to bring the user back to the are you a vendor question
                        break  # breaks out of the purchase while loop
                    fiveInput = enterInt("Enter no. of $5 notes: ", "Error, please enter a valid number.")  # calling to function to validate customer's input with two arguments instead of crashing the program
                    totalAmt += fiveInput*5
                    if totalAmt >= totalPrice:  # checks if the user has paid the sufficient amount
                        userChange = totalAmt - totalPrice
                        if userChange > 0:  # checking if there any change for the customer to take, if there is $0 in change, it will not display the message below
                            print("Please collect your change: $%.2f" % userChange)
                        print("Drinks paid. Thank you.\n\n")
                        userstatus = False  # make condition false to bring the user back to the are you a vendor question
                        break # breaks out of the purchase while loop
                    twoInput = enterInt("Enter no. of $2 notes: ", "Error, please enter a valid number.")  # calling to function to validate customer's input with two arguments instead of crashing the program
                    totalAmt += twoInput*2
                    if totalAmt >= totalPrice:  # checks if the user has paid the sufficient amount
                        userChange = totalAmt - totalPrice
                        if userChange > 0:  # checking if there any change for the customer to take, if there is $0 in change, it will not display the message below
                            print("Please collect your change: $%.2f" % userChange)
                        print("Drinks paid. Thank you.\n\n")
                        userstatus = False  # make condition false to bring the user back to the are you a vendor question
                        break  # breaks out of the purchase while loop
                    print("\nNot enough to pay for the drinks\nTake back your cash!\n")
                else:
                    print("Invalid input.")  # prints an error message if user inputs did not input "N", "n", "Y", or "y"
                cancelPurchase = input("Do you want to cancel the purchase? Y/N: ").upper()  # the while loop condition will become false and stop if user inputs "y" or "Y", else, it will keep looping if user inputs "n" or "N"
                if cancelPurchase == "Y":
                    print("Purchase is cancelled. Thank you.\n\n")

        elif question == "Y":
            vendorChoice = ""
            while vendorChoice != "0":
                print(vendorMenu)
                vendorChoice = input("Enter choice: ")
                if vendorChoice == "1":
                    # Add new drink type
                    print("You have chosen to add a new drink type!")  # a placeholder for the actual code for part 2
                elif vendorChoice == "2":
                    # Replenish drink
                    print("You have chosen to replenish a drink!")  # a placeholder for the actual code for part 2
                elif vendorChoice == "0":
                    print("You have exited the vendor's menu.")
                else:
                    print("Invalid option.")
            break  # breaks out to the are you a vendor question
        else:
            print("Invalid option.")
            break  # breaks out to the are you a vendor question
