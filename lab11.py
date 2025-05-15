import datetime

expenses = []

def add_expense():
    print("\n---- Add New Expense ----")
    date_str = input("Enter date (YYYY-MM-DD): ")
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    category = input("Enter category: ")
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be positive.")
            else:
                break
        except ValueError:
            print("Invalid amount. Please enter a number.")

    description = input("Enter description: ")
    expenses.append({"date": date, "category": category, "amount": amount, "description": description})
    print("Expense added successfully!\n")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.\n")
        return
    print("\n---- All Expenses ----")
    for i, expense in enumerate(expenses):
        print(f"Entry {i+1}:")
        for key, value in expense.items():
            print(f"{key.capitalize()}: {value}")
        print("----------------------")
    print()

def total_category_expenses():
    category_to_find = input("Enter category to see total expenses: ")
    total = 0
    found = False
    for expense in expenses:
        if expense["category"].lower() == category_to_find.lower():
            total += expense["amount"]
            found = True
    if found:
        print(f"Total expenses for '{category_to_find}': ${total:.2f}\n")
    else:
        print(f"No expenses found for the category '{category_to_find}'.\n")

def delete_expense():
    view_expenses()
    if not expenses:
        return
    while True:
        try:
            entry_num_str = input("Enter the entry number to delete: ")
            entry_num = int(entry_num_str)
            if 1 <= entry_num <= len(expenses):
                deleted_expense = expenses.pop(entry_num - 1)
                print(f"Expense '{deleted_expense['description']}' deleted successfully!\n")
                break
            else:
                print("Invalid entry number. Please enter a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main_menu():
    while True:
        print("===== Simple Expense Tracker =====")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. See Total Category Expenses")
        print("4. Delete an Expense")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_category_expenses()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            print("Thank you for using the Expense Tracker!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main_menu()
