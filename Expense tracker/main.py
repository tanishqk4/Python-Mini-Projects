expenses = [] #list of all expanses(it will be in form of dictionary)
print("Welcome to Your Expense Tracker!")

while True:
    print("--MENU--")
    print("1. Add your expense")
    print("2. View your all expenses")
    print("3. View Total expense")
    print("4. Exit")

    choice = int(input("What's new?(choose any one option)"))


    #1. Add your expense
    if(choice == 1):
        date = input("Enter the date:")
        category = input("Choose Category(Food, Travel, Rent, etc.)")
        description = input("Add discription:")
        amount = float(input("Enter Amount:"))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense)
        print("Done! Expenses added.")

    #2. View All your expenses
    elif (choice== 2):
        if len(expenses) == 0:
            print("NO expenses added!")
        else:
            count = 1
            for each in expenses:
                print(f"{count} -> {each["date"]}, {each["category"]}, {each["description"]}, {each["amount"]}")
                count = count + 1

    #3. View Total expense
    elif (choice == 3):
        total = 0
        for each in expenses:
            total = total + each["amount"]
        print("Total Expenses are ", total)

    #4. Exist
    elif(choice == 4):
        print("Thankyou For using!")
        break
    else:
        print("Invalid input")
        

