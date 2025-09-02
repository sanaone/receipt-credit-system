from tabulate import tabulate
import json

# Load customers from JSON file, or create a default list if file not found
def load_customers():
    try:
        with open("customers.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return [
            {"Name": "John", "Balance": 0},
            {"Name": "Kumar", "Balance": 0},
            {"Name": "Sanath", "Balance": 0},
            {"Name": "Paul", "Balance": 0}
        ]
def reset_customers():
    customers = [
        {"Name": "John", "Balance": 0},
        {"Name": "Kumar", "Balance": 0},
        {"Name": "Sanath", "Balance": 0},
        {"Name": "Paul", "Balance": 0}
    ]
    save_customers(customers)
    Customers =load_customers()
    return "Customer data reset to default."
# Save customers to JSON file
def save_customers(customers):
    with open("customers.json", "w") as f:
        json.dump(customers, f, indent=4)

def deposit(name, amount):
    for customer in Customers:
        if customer["Name"] == name:
            customer["Balance"] += amount
            save_customers(Customers)   # save after deposit
            return f"Deposit of {amount} successful. New balance of {customer['Name']} is {customer['Balance']}"
    return f"Customer {name} not found"

def withdraw(name, amount):
    for customer in Customers:
        if customer["Name"]== name:
            if customer["Balance"]>= amount:
                customer["Balance"] -= amount
                save_customers(Customers)  # save after withdrawal
                return f"Withdrawal of {amount} successful. New balance of {customer['Name']} is {customer['Balance']}"
            else:
                return f"Insufficient balance for {customer['Name']}. Current balance is {customer['Balance']}"
    return (f"Customer {name} not found")

def view_balance(name):
    """Return the balance for a single customer"""
    customers = load_customers()
    for customer in customers:
        if customer["Name"] == name:
            return f"{customer['Name']}'s balance is {customer['Balance']}"
    return f"Customer {name} not found"
     
def list_all_balances(pretty=False):
    """Return balances for all customers"""
    Customers = load_customers()
    if pretty:
        table = [(c["Name"], c["Balance"]) for c in Customers]
        return tabulate(table, headers=["Name", "Balance"], tablefmt="grid")
    else:
        return Customers
Customers =load_customers()

receipt_text = """
Customer: John
Items:
- Apples: 50
- Bread: 20
Total: 70
"""
def parse_receipt(text):
    lines = text.strip().split("\n")
    customerName = lines[0].split(": ")[1]
    total = int(lines[-1].split(": ")[1])
    return customerName, total

name, amount = parse_receipt(receipt_text)
print(f"Parsed receipt - Customer: {name}, Amount: {amount}")
deposit(name, amount)

# Test it


# View all balances (pretty)
print("All balances (pretty):")
print(list_all_balances(pretty=True))
