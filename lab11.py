import datetime

class Expense:
    def __init__(self, date, category, amount, description):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def __str__(self):
        return (f"Date       : {self.date}\n"
                f"Category   : {self.category}\n"
                f"Amount     : ${self.amount:.2f}\n"
                f"Description: {self.description}")

expenses = []

def get_valid_date(prompt="Enter date (YYYY-MM-DD): "):
    while True:
        date_str = input(prompt)
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("✗ Invalid date format. Please use YYYY-MM-DD.")

def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount > 0:
                return amount
            else:
                print("✗ Amount must be positive.")
        except ValueError:
            print("✗ Invalid amount. Please enter a number.")

def add_expense():
    print("\n---- Add New Expense ----")
    date = get_valid_date()

    if expenses:
        existing_categories = list({e.category for e in expenses})
        print(f"Existing categories: {', '.join(existing_categories)}")
    category = input("Enter category: ")

    amount = get_valid_amount()
    description = input("Enter description: ")

    expenses.append(Expense(date, category, amount, description))
    print("✓ Expense added successfully!\n")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    print("\n---- All Expenses ----")
    for i, expense in enumerate(expenses, 1):
        print(f"Entry {i}:")
        print(expense)
        print("-" * 30)
    print()

def total_category_expenses():
    category_to_find = input("Enter category to see total expenses: ")
    total = sum(e.amount for e in expenses if e.category.lower() == category_to_find.lower())

    if total > 0:
        print(f"✓ Total expenses for '{category_to_find}': ${total:.2f}\n")
    else:
        print(f"✗ No expenses found for the category '{category_to_find}'.\n")

def delete_expense():
    view_expenses()
    if not expenses:
        return
    while True:
        try:
            entry_num = int(input("Enter the entry number to delete: "))
            if 1 <= entry_num <= len(expenses):
                deleted_expense = expenses.pop(entry_num - 1)
                print(f"✓ Expense '{deleted_expense.description}' deleted successfully!\n")
                break
            else:
                print("✗ Invalid entry number. Please try again.")
        except ValueError:
            print("✗ Invalid input. Please enter a number.")

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
            print("✓ Thank you for using the Expense Tracker!")
            break
        else:
            print("✗ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main_menu()
