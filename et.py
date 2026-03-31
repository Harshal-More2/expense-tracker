from datetime import datetime

expenses = []
total = 0

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. Delete Expense")
    print("3. Show Expenses")
    print("4. Exit")

    choice = input("Enter Choice = ")

    if choice == "1":
        name = input("Enter Name: ")
        amount = int(input("Enter Amount: "))
        category = input("Enter Category: ")
        date = datetime.now().strftime("%d-%m-%Y %H:%M")
        expenses.append((name, amount, category, date))
        total += amount
        print("Expense added!")
        print("Added on:", date)
        print("Current Total:", total)

    elif choice == "2":
        if len(expenses) == 0:
            print("⚠ No expenses to delete")
        else:
            print("\nYour Expenses:")
            for i, exp in enumerate(expenses):
                print(i, "->", exp)

            index = int(input("Enter index to delete: "))

            if 0 <= index < len(expenses):
                total -= expenses[index][1]
                expenses.pop(index)
                print("Expense deleted!")
                print("Updated Total:", total)
            else:
                print("Invalid index")

    elif choice == "3":
        if len(expenses) == 0:
            print("No expenses added yet.")
        else:
            print("\nYour Expenses:")
            for exp in expenses:
                print("Name:", exp[0],
                      "| Amount:", exp[1],
                      "| Category:", exp[2],
                      "| Date & Time:", exp[3])

            print("Total Expense:", total)

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
