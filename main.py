from tabulate import tabulate
import json
import re
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
            log_transaction(name,amount,"Deposit")
            
            return f"Deposit of {amount} successful. New balance of {customer['Name']} is {customer['Balance']}"
    return f"Customer {name} not found"

def withdraw(name, amount):
    for customer in Customers:
        if customer["Name"]== name:
            if customer["Balance"]>= amount:
                customer["Balance"] -= amount
                save_customers(Customers)  # save after withdrawal
                log_transaction(name,amount,"Withdraw")
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
Customer Name: Kumar
Items:
- Apples: 50
- Bread: 20
Total: 10
"""
def parse_receipt(receipt_text):
    # Match "Customer:" OR "Customer Name:" (case-insensitive)
    name_match = re.search(r"Customer(?: Name)?:\s*(\w+)", receipt_text, re.IGNORECASE)
    # Match "Total:" OR "Total Amount:" 
    total_match = re.search(r"Total(?: Amount)?:\s*(\d+)", receipt_text, re.IGNORECASE)

    if not name_match or not total_match:
        return "Invalid receipt format."

    name = name_match.group(1)
    total = int(total_match.group(1))
    return name, total
def process_receipt(receipt_text):
    result = parse_receipt(receipt_text)
    if isinstance(result, str):
        return result  # error message
    
    name, total = result
    return deposit(name, total)
  
#print(f"Parsed receipt - Customer: {name}, Amount: {amount}")


def log_transaction(name, amount, transaction_type):
    try:
        with open("transactions.json", "r") as f:
            transactions = json.load(f)

    except FileNotFoundError:
        transactions = []
    transactions.append({"Name": name, "Amount": amount, "Type": transaction_type})
    with open("transactions.json", "w") as f:
        json.dump(transactions, f, indent=4)

def view_transactions(name=None, pretty=None):
    try:
        with open("transactions.json", "r") as f:
            transactions = json.load(f)
    except FileNotFoundError:
        return "No transactions yet."
    
    if name:
        transactions = [t for t in transactions if t["Name"] == name]
    
    if pretty:
        table = [(t["Name"], t["Amount"], t["Type"]) for t in transactions]
        
        print("DEBUG table:", table)
        return tabulate(table, headers=["Name", "Amount", "Type"], tablefmt="grid")
    else:
        return transactions
     

print(process_receipt(receipt_text)) 
print(view_transactions(pretty=True))
# View all balances (pretty)
print("All balances (pretty):")
print(list_all_balances(pretty=True))
