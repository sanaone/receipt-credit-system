from tabulate import tabulate
import json
import re
import datetime
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
            
            return f"Deposit of RS. {amount} successful. New balance of {customer['Name']} is {customer['Balance']}"
    return f"Customer {name} not found"

def withdraw(name, amount):
    for customer in Customers:
        if customer["Name"]== name:
            if customer["Balance"]>= amount:
                customer["Balance"] -= amount
                save_customers(Customers)  # save after withdrawal
                log_transaction(name,-amount,"Withdraw")
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
    transactions.append({
        "Name": name,
        "Amount": amount,
        "Type": transaction_type,
        "Timestamp": __import__("datetime").datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    with open("transactions.json", "w") as f:
        json.dump(transactions, f, indent=4)

def view_transactions(name=None, pretty=None, Type_Transaction=None):
    try:
        with open("transactions.json", "r") as f:
            transactions = json.load(f)
    except FileNotFoundError:
        return "No transactions yet."
    
    if name:
        transactions = [t for t in transactions if t["Name"] == name]
    if Type_Transaction:
        transactions = [t for t in transactions if t["Type"] == Type_Transaction]
    if not transactions:
        return "No matching transactions found."
    
    if pretty:
        table = [
            (t.get("Name", "N/A"),
             t.get("Amount", "N/A"),
             t.get("Type", "N/A"),
             t.get("Timestamp", "N/A"))   # fallback if missing
            for t in transactions
        ]
        return tabulate(table, headers=["Name", "Amount", "Type", "Timestamp"], tablefmt="grid")
    else:
        return transactions
     
def filter_by_date(transaction_s, start_date=None, end_date=None):
    """Filter Transactions by date range.
    Dates should be in YYYY-MM-DD format."""
    filtered = []
    for t in transaction_s:
        t["Timestamp"]= t.get("Timestamp", "2025-09-05 00:00:00")  # Handle missing timestamp
        t_date = datetime.datetime.strptime(t["Timestamp"], "%Y-%m-%d %H:%M:%S").date()
        if start_date:
            start = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()  # FIXED
            if t_date < start:
                continue
        if end_date:
            end = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
            if t_date > end:
                continue
        filtered.append(t)
    return filtered

def view_transactions_per_customer(pretty=False):
    #Load transactions
    try:
        with open("transactions.json", "r") as f:
            transactions= json.load(f)
    except FileNotFoundError:
        return "No transactions yet."
    # Track balances per customer
    customer_balances  ={}
    table =[]
    transactions = filter_by_date(transactions, start_date="2025-09-04", end_date="2025-09-05")
    for t in transactions:
        
        name = t["Name"]
        amount = t["Amount"]
        t["Timestamp"]= t.get("Timestamp", "2025-09-06 00:00:00")  # Handle missing timestamp
        customer_balances[name] = customer_balances.get(name, 0) + amount
        table.append((
            t["Name"],
            t["Amount"],
            t["Type"],
            t["Timestamp"],
            customer_balances[name]
        ))

    if pretty:
        return tabulate(table,headers=["Name","Amount","Type", "Timestamp","Balance"],tablefmt="grid")
    else:
        return table
    
#print(process_receipt(receipt_text)) 

print(reset_customers())
deposit("John", 100)
withdraw("John", 40)
deposit("Kumar", 200)
deposit("John", 50)
withdraw("Kumar", 30)

print("Transactions with per-customer running balance:")
print(view_transactions_per_customer(True))

#print("All transactions with Timestamps:")
 

#print(view_transactions(pretty=True))
#print(view_transactions(pretty=True))
# View all balances (pretty)
#print("All balances (pretty):")
#print(list_all_balances(pretty=True))
