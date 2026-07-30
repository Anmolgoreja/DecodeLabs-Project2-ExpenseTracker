# Project 2 - Expense Tracker
# DecodeLabs Python Programming Internship
# Batch: 2026

print("EXPENSE TRACKER")

total = 0.0
expense_count = 0

while True:
    print("\n1. Add Expense")
    print("2. View Total Spent")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        while True:
            try:
                expense = float(input("Enter expense amount: "))

                if expense < 0:
                    print("Expense cannot be negative.")
                    continue

                if expense == 0:
                    print("Expense must be greater than 0.")
                    continue

                total = total + expense
                expense_count = expense_count + 1

                print(f"Expense added successfully: {expense:.2f}")
                print(f"Current Total Spent: {total:.2f}")

                break

            except ValueError:
                print("Invalid input. Please enter a valid number.")

    elif choice == "2":
        if expense_count == 0:
            print("No expenses have been added yet.")
        else:
            print(f"Number of Expenses: {expense_count}")
            print(f"Total Spent: {total:.2f}")

    elif choice == "3":
        print(f"Final Total Spent: {total:.2f}")
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")