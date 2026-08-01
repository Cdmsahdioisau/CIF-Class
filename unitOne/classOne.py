#Lists
breadTypes = ["White Bread",
                "Whole Wheat Bread",
                "Sourdough",
                "Rye Bread",
                "Multigrain Bread",
                "Special Bagel"]
breadCosts = ["2.25",
                "3.75", 
                "4.00",
                "3.00", 
                "3.50", 
                "723.25"]

#Starter Variables
discount = 0
totalCost = 0

#Ordering Checker
ordering = True

#Welcome Message
print("Welcome to BREAD!\nIn BREAD, we sell bread because bread is goated.\nPlease choose a bread you want down below")

#Print Lists
for i, bread in enumerate(breadTypes):
    print(f"{i + 1}. {bread} ${breadCosts[i]}")

#Give Discount or No
CIFStudent = input("Are you a CIF Student? (y/n)")

if CIFStudent.lower() == "y":
    discount = 0.1
    print(f"You get a 10% discount on your purchases!")
elif CIFStudent.lower() == "n":
    discount = 0
    print(f"You do not get a discount on your purchases.")

#Ordering Loop
while ordering:
    #Order Variables
    breadType = input("Choose the bread number you want: ")
    breadNumber = input("Choose how much you want in numbers:")

    #Calculate Cost of Order
    nowCost = (float(breadNumber) * float(breadCosts[int(breadType) - 1])) * (1 - discount)
    nowCost = round(nowCost, 2)

    #Ask to accept order
    acceptOrder = input(f"Buying {breadNumber} {breadTypes[int(breadType) - 1]}(s) will cost you ${nowCost}, do you want to continue? (y/n)")

    if acceptOrder.lower() == "y":
        totalCost += nowCost
        continueOrdering = input("Do you want to continue ordering? (y/n)")

        #Check if they want to order something else
        if continueOrdering.lower() == "y":
            ordering = True

            for i, bread in enumerate(breadTypes):
                print(f"{i + 1}. {bread} ${breadCosts[i]}")

        elif continueOrdering.lower() == "n":
            ordering = False
            print(f"Your total cost is {totalCost}!")
        
    elif acceptOrder.lower() == "n":
        print("Your Order has been canceled")

        #Check if they still want to order something else
        continueOrdering = input("Do you want to continue ordering? (y/n)")

        if continueOrdering.lower() == "y":
            ordering = True
        
            for i, bread in enumerate(breadTypes):
                print(f"{i + 1}. {bread} ${breadCosts[i]}")
        
        elif continueOrdering.lower() == "n":
            ordering = False

            print(f"Your total cost is {totalCost}!")
    


    
