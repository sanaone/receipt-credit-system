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

# Save customers to JSON file
def save_customers(customers):
    with open("customers.json", "w") as f:
        json.dump(customers, f, indent=4)

Customers = load_customers()

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

# Test it
print(deposit("John", 50))
print(withdraw("Kumar", 30))
print(Customers)
