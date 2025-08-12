import json
import os

FILE_NAME = "expenses.json"

# Load expenses from file
def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save expenses to file
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

# Add new expense
def add_expense(name, amount):
    expenses = load_expenses()
    expenses.append({"name": name, "amount": amount})
    save_expenses(expenses)
    print(f"✅ Added expense: {name} - {amount}")

# View all expenses
def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return
    print("\nExpenses:")
    for e in expenses:
        print(f"- {e['name']}: {e['amount']}")

# Delete expense by name
def delete_expense(name):
    expenses = load_expenses()
    updated = [e for e in expenses if e["name"].lower() != name.lower()]
    if len(updated) == len(expenses):
        print(f"❌ No expense found with name '{name}'")
    else:
        save_expenses(updated)
        print(f"🗑️ Deleted expense: {name}")

# Main program loop
while True:
    print("\n1. Add Expense\n2. View Expenses\n3. Delete Expense\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        add_expense(name, amount)
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        name = input("Enter name to delete: ")
        delete_expense(name)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Try again.")
