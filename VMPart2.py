# Author: Kuan Jun Hao Jason
# Admin No: 201484K

import copy  # import copy for copy.deepcopy() as to copy the nested dictionary value/strings as compared to .copy()/shallow copying

def enterFloat(prompt, error):
    # for float data type validation check
    continueLoop = True
    while continueLoop:
        try:
            thevalue = float(input(prompt))
            if thevalue >= 0:
                return thevalue  # return the value if it is a float data type and is more than or equal to 0
            else:
                print(error)
        except:
            print(error)

def enterInt(prompt, error):
    # for integer data type validation check
    continueLoop = True
    while continueLoop:
        try:
            thevalue = int(input(prompt))
            if thevalue >= 0:
                return thevalue  # return the value if it is a int data type and is more than or equal to 0
            else:
                print(error)
        except:
            print(error)

def enterPrice(prompt):
    # for float data type validation check and ensuring that the price is more than 0 dollars when vendor is adding a new drink type
    continueLoop = True
    while continueLoop:
        try:
            thevalue = float(input(prompt))
            if thevalue > 0:
                return thevalue  # return the value if it is a int data type and is more than 0
            elif thevalue == 0 :
                print("Please enter a price more than $0.00!")
            else:
                print("Please enter a positive value for the price!")
        except:
            print("Please enter a number for the price!")

def enterInput(prompt, error):
    # validation check to ensure entered input is not empty
    continueLoop = True
    while continueLoop:
        theinput = input(prompt).strip()  # .strip() to remove any whitespace characters at the start and at the end of the string
        # checks if the input length is more than 0
        if len(theinput) != 0:
            return theinput
        else:
            print(error)

def enterInputId(prompt):
    # validation check to ensure entered input is not empty
    continueLoop = True
    while continueLoop:
        theinput = input(prompt)
        theinput = ''.join(theinput.split())  # removes all whitespace characters and spilt them into a list, then joins them back into a string, e.g. " I  M  " will become "IM"
        if len(theinput) != 0:
            return theinput
        else:
            print("Input cannot be empty!")

def printInventory():
    # Printing the inventory on the vendor's side
    # inventory will be updated when customer has confirmed his/her purchase
    maxLength = 0
    for key in drinksDict:
        # to get the longest string length to align the Qty on the same column when printing the list of drinks
        drinkId = key + ". "
        drinkDesc = drinksDict[key]["description"]
        drinkPrice = drinksDict[key]["price"]
        roundDrinkPrice = " ($%.2f) " % drinkPrice
        combinedString = drinkId + drinkDesc + roundDrinkPrice
        lengthToCheck = len(combinedString)
        if lengthToCheck > maxLength:  # if statement to check if the current key's combined string is longer than the previous
            maxLength = lengthToCheck  # if so, maxLength will update to the longest key's length
    for key in drinksDict:
        # print the inventory dictionary to a readable format
        drinkId = key + ". "
        drinkDesc = drinksDict[key]["description"]
        drinkPrice = drinksDict[key]["price"]
        roundDrinkPrice = " ($%.2f) " % drinkPrice
        qty = drinksDict[key]["quantity"]
        if qty > 0:  # checking for the quantity if it is out of stock
            drinkQty = "Qty: " + str(drinksDict[key]["quantity"])
        else:
            drinkQty = "***out of stock***"
        combinedString = drinkId + drinkDesc + roundDrinkPrice
        print(combinedString.ljust(maxLength) + drinkQty)  # l.just(maxLength) to align the Qty on the same column on the output

def printCart():
    # printing the list of drinks for the customer and acts as a placeholder which will only update the drinksDict when the customer has confirmed his/her purchase
    # else, it will reset back to the original drinksDict if purchase was not confirmed
    maxLength = 0
    for key in cartDict:
        # to get the longest string length to align the Qty on the same column when printing the list of drinks
        drinkId = key + ". "
        drinkDesc = cartDict[key]["description"]
        drinkPrice = cartDict[key]["price"]
        roundDrinkPrice = " ($%.2f) " % drinkPrice
        combinedString = drinkId + drinkDesc + roundDrinkPrice
        lengthToCheck = len(combinedString)
        if lengthToCheck > maxLength:  # if statement to check if the current key's combined string is longer than the previous
            maxLength = lengthToCheck  # if so, maxLength will update to the longest key's length
    for key in cartDict:
        # print the inventory dictionary to a readable format
        drinkId = key + ". "
        drinkDesc = cartDict[key]["description"]
        drinkPrice = cartDict[key]["price"]
        roundDrinkPrice = " ($%.2f) " % drinkPrice
        qty = cartDict[key]["quantity"]
        if qty > 0:  # checking for the quantity if it is out of stock
            drinkQty = "Qty: " + str(cartDict[key]["quantity"])
        else:
            drinkQty = "***out of stock***"
        combinedString = drinkId + drinkDesc + roundDrinkPrice
        print(combinedString.ljust(maxLength) + drinkQty)  # l.just(maxLength) to align the Qty on the same column on the output

def add_drink_type(drink_id, description, price, quantity):
    # For adding new drinks on the vendor's side
    newDrinkDict = {}  # creates a new dictionary to nest it inside drinksDict
    newDrinkDict["description"] = description
    newDrinkDict["price"] = price
    newDrinkDict["quantity"] = quantity
    drinksDict[drink_id] = newDrinkDict  # adds the new dictionary, newDrinkDict to the existing drinksDict dictionary.
    print("Drinks added!\n\n")

def replenish_drink(drink_id, quantity):
    # For replenishing the drinks on the vendor's side
    drinksDict[drink_id]["quantity"] += quantity  # adds the quantity to update the respective drink id's quantity to drinksDict
    drinkName = drinksDict[drink_id]["description"]
    print(drinkName, "has been top up!\n\n")

def update_qty(drink_id):
    # for updating the customer's drinks menu quantity before confirming their purchase/while the customer is selecting his/her drink(s)
    cartDict[drink_id]["quantity"] -= 1  # minus the quantity in the drinkCart by 1 when user has selected the corresponding drink


drinksDict = {
    'IM': {'description': 'Iced Milo', 'price': 1.5, 'quantity': 30},
    'HM': {'description': 'Hot Milo', 'price': 1.2, 'quantity': 40},
    'IC': {'description': 'Iced Coffee', 'price': 1.5, 'quantity': 50},
    'HC': {'description': 'Hot Coffee', 'price': 1.2, 'quantity': 20},
    '1P': {'description': '100 Plus', 'price': 1.1, 'quantity': 1},
    'CC': {'description': 'Coca Cola', 'price': 1.3, 'quantity': 5},
}

vendorMenu = """\nWelcome to ABC Vending Machine.
Select from following choices to continue:
1. Add Drink Type
2. Replenish Drink
3. Display Inventory
4. Shut Down Vending Machine
0. Exit"""

## GENERAL LOOP ##
loop = True  # Will remain true forever when the program is running
## END OF GENERAL LOOP ##

## VENDOR'S MENU LOOPS ##
drinkAdd = True  # Will remain true forever when the program is running
replenish = True  # Will remain true forever when the program is running
loop_shut_down = True  # Will remain true forever when the program is running
## END OF VENDOR'S MENU LOOPS ##

while loop:
    question = enterInput("Are you a vendor (Y/N)?: ", "Input cannot be empty!").upper()
    userstatus = True
    while userstatus:
        if question == "N":
            choice = ""  # to reset the choice to an empty string for the main while loop below, "while choice != "0":"
            cancelPurchase = "N"  # to reset the cancelPurchase back to "N" for the purchase loop to loop
            userQuantity = 0  # to reset the total number of selected drinks
            totalPrice = 0  # to reset the total price of the selected drinks
            totalAmt = 0  # to reset the amount of money paid by the customer
            cartDict = copy.deepcopy(drinksDict)  # copies the drinksDict dictionary and its nested dictionary values/strings to reset the quantities in the menu if the customer did not buy anything or cancel their purchase
            while choice != "0":
                print("\nWelcome to ABC Vending Machine.\nSelect from following choices to continue:")
                printCart()  # calls out the function to print the menu
                print("0. Exit / Payment")
                userChoice = enterInputId("Enter choice: ").upper()
                if userChoice in drinksDict:
                    qtyCheck = cartDict[userChoice]["quantity"]  # retrieves the quantity in the cartDict
                    drinkName = drinksDict[userChoice]["description"]  # retrieves the description of the drink in the original drinksDict
                    itemQty = 0  # resets to zero as to prevent the quantity from reaching more than 1
                    if qtyCheck > 0:
                        userQuantity += 1  # add to the total number of selected drinks
                        print("No. of drinks selected =", userQuantity)
                        itemQty += 1  # for updating the quantity in the menu
                        totalPrice += drinksDict[userChoice]["price"]  # adds the price of the drink to the total amount of money that the customer has to pay
                        update_qty(userChoice)  # calls out the function, update_qty, to minus the quantity in the customer's menu by 1 according to the customer's inputted drink_id which is the argument for the function.
                    else:
                        print(drinkName, "is out of stock")
                elif userChoice == "0":
                    choice = "0"  # while condition will become false and stops
                else:
                    print("Your selected choice is not in the list.")  # prints a error message if user inputs an invalid id
            if totalPrice == 0:
                print("Thank you and have a nice day!\n")
                break  # breaks out of the loop if customer did not buy anything or if the customer wants to exit to the "Are you a vendor..." question
            while cancelPurchase != "Y":
                if cancelPurchase == "N":
                    print("\n\nPlease pay: $%.2f\nIndicate your payment:" % totalPrice)
                    tenInput = enterInt("Enter no. of $10 notes: ", "Error, please enter a valid number.")
                    totalAmt += tenInput*10
                    if totalAmt >= totalPrice:  # checks if the user has paid the sufficient amount
                        userChange = totalAmt - totalPrice
                        if userChange > 0:  # checking if there any change for the customer to take, if there is $0 in change, it will not display the message below
                            print("Please collect your change: $%.2f" % userChange)
                        print("Drinks paid.\nThank you and have a nice day!\n\n")
                        drinksDict = cartDict.copy()  # copies the placeholder dictionary/inventory, cartDict to update the drinksDict's quantity as the customer have confirmed his/her purchase
                        userstatus = False  # make condition false to bring the user back to the are you a vendor question
                        break  # breaks out of the purchase while loop
                    fiveInput = enterInt("Enter no. of $5 notes: ", "Error, please enter a valid number.")
                    totalAmt += fiveInput*5
                    if totalAmt >= totalPrice:  # checks if the user has paid the sufficient amount
                        userChange = totalAmt - totalPrice
                        if userChange > 0:  # checking if there any change for the customer to take, if there is $0 in change, it will not display the message below
                            print("Please collect your change: $%.2f" % userChange)
                        print("Drinks paid.\nThank you and have a nice day!\n\n")
                        drinksDict = cartDict.copy()  # copies the placeholder dictionary/inventory, cartDict to update the drinksDict's quantity as the customer have confirmed his/her purchase
                        userstatus = False  # make condition false to bring the user back to the are you a vendor question
                        break  # breaks out of the purchase while loop
                    twoInput = enterInt("Enter no. of $2 notes: ", "Error, please enter a valid number.")
                    totalAmt += twoInput*2
                    if totalAmt >= totalPrice:  # checks if the user has paid the sufficient amount
                        userChange = totalAmt - totalPrice
                        if userChange > 0:  # checking if there any change for the customer to take, if there is $0 in change, it will not display the message below
                            print("Please collect your change: $%.2f" % userChange)
                        print("Drinks paid.\nThank you and have a nice day!\n\n")
                        drinksDict = cartDict.copy()  # copies the placeholder dictionary/inventory, cartDict to update the drinksDict's quantity as the customer have confirmed his/her purchase
                        userstatus = False  # make condition false to bring the user back to the are you a vendor question
                        break  # breaks out of the purchase while loop
                    print("\nNot enough to pay for the drinks\nTake back your cash!\n")
                else:
                    print("Invalid input.")  # prints an error message if user inputs did not input "N", "n", "Y", or "y"
                cancelPurchase = enterInput("Do you want to cancel the purchase? Y/N: ", "Input cannot be empty!").upper()  # the while loop condition will become false and stop after executing the last 2 lines after this line if user inputs "y" or "Y", else, it will keep looping if user inputs "n" or "N"
                if cancelPurchase == "Y":  # if user enters "y" or "Y", it will print the message below to indicate that the purchase has been cancelled
                    print("Purchase is cancelled. Thank you.\n\n")

        elif question == "Y":
            vendorChoice = ""
            while vendorChoice != "0":
                print(vendorMenu)
                vendorChoice = enterInput("Enter choice: ", "Input cannot be empty!")
                if vendorChoice == "1":
                    # add drink type
                    while drinkAdd:
                        drinkId = enterInputId("Enter drink id (0 to cancel): ")
                        if drinkId == "0":
                            print("Adding of new drink has been cancelled.")
                            break
                        drinkId = drinkId.upper()
                        if drinkId not in drinksDict:
                            drinkDesc = enterInput("Enter description of drink: ", "Description cannot be empty!").title()
                            drinkPrice = enterPrice("Enter price: $")
                            drinkQty = enterInt("Enter quantity: ", "Error in entered quantity!")
                            add_drink_type(drinkId, drinkDesc, drinkPrice, drinkQty)  # calls out the function to add a new drink type
                        else:
                            print("Drink id exists!")
                        break
                elif vendorChoice == "2":
                    # Replenish drink
                    printInventory()
                    while replenish:
                        drinkId = enterInputId("Enter drink id (0 to cancel): ").upper()
                        if drinkId == "0":
                            print("Drink replenishment has been cancelled.")
                            break
                        if drinkId in drinksDict:
                            qtyCheck = drinksDict[drinkId]["quantity"]
                            if qtyCheck <= 5:  # checks if the quantity is less than or equal to 5 as needed in the technical requirement
                                drinkQty = enterInt("Enter quantity: ", "Error in entered quantity!")
                                replenish_drink(drinkId, drinkQty)  # calls out the function to replenish the existing drinks
                                break
                            else:
                                print("No need to replenish. Quantity is greater than 5.")  # prints an error message if the quantity is already greater than 5
                                break
                        else:
                            print("Drink id not found.\n")  # prints an error message if drink id is not found in the drinksDict
                elif vendorChoice == "3":
                    # Display the inventory as the only way to display the inventory is through replenishing the drinks
                    # hence, a display inventory option would be useful if the vendor just wants to check the inventory
                    printInventory()
                elif vendorChoice == "4":
                    # Shut down the vending machine if the vendor wish to do so
                    confirm_vendor_input = ""
                    while loop_shut_down:
                        confirm_vendor_input = enterInput("Are you sure that you would like to shut down the vending machine? (Y/N): ", "Input cannot be empty!").upper()
                        if confirm_vendor_input == "Y":
                            loop = False
                            print("\nThe vending machine will now proceed to shut down.")
                            break
                        elif confirm_vendor_input == "N":
                            print("\nThe vending machine will continue to operate as normal.")
                            break
                        else:
                            print("Invalid option.")
                    if confirm_vendor_input == "Y":
                        break  # break out from the vendor's menu loop
                elif vendorChoice == "0":
                    print("You have exited the vendor's menu.\n")
                else:
                    print("Invalid choice.")  # prints an error message if the vendor inputs a message other than 1, 2, 3, or 0.
            break  # breaks out of the loop if the vendor wants to exit to the "Are you a vendor..." question
        else:
            print("Invalid input.")  # prints an error message if the user enters an input other than "Y", "y", "N", or "n"
            break  # break out of the loop to the "Are you a vendor..." question
