# src/main.py
import csv
from pathlib import Path

CSV_FILE = Path(__file__).resolve().parents[0] / "expenses.csv"
FIELDNAMES = ["id", "name", "amount"]

def ensure_csv():
    if not CSV_FILE.exists():
        with CSV_FILE.open("w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()

def add_expense(name, amount):
    ensure_csv()
    rows = list(read_all())
    next_id = (int(rows[-1]["id"]) + 1) if rows else 1
    with CSV_FILE.open("a", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writerow({"id": next_id, "name": name, "amount": f"{amount:.2f}"})
    print(f"Added: {name} — ₹{amount:.2f}")

def read_all():
    if not CSV_FILE.exists():
        return []
    with CSV_FILE.open("r", newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

def show_expenses():
    rows = read_all()
    if not rows:
        print("No expenses yet.")
        return
    total = 0.0
    print("\nExpenses:")
    for r in rows:
        amt = float(r["amount"])
        total += amt
        print(f"{r['id']:>3}  {r['name']:<20} ₹{amt:.2f}")
    print(f"\nTotal: ₹{total:.2f}")

def delete_expense(expense_id):
    rows = read_all()
    new = [r for r in rows if r["id"] != str(expense_id)]
    if len(new) == len(rows):
        print("No matching id found.")
        return
    with CSV_FILE.open("w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(new)
    print(f"Deleted id {expense_id}")

def cli():
    ensure_csv()
    while True:
        print("\nCommands: add, list, del, exit")
        cmd = input("cmd> ").strip().lower()
        if cmd == "add":
            name = input("name: ").strip()
            amt = float(input("amount: ").strip())
            add_expense(name, amt)
        elif cmd == "list":
            show_expenses()
        elif cmd == "del":
            eid = input("id to delete: ").strip()
            delete_expense(eid)
        elif cmd in ("exit", "quit"):
            break
        else:
            print("unknown command")

if __name__ == "__main__":
    cli()
