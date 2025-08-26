print("Hello, world!")
x = 10
name ="sandip kumar" 
price = 9.99

print(x)
print(name)
print(price)

# list
fruits  = ["apple", "banana", "cherry"]
 
for item in fruits:
     print(item) 

# dictionary
customers = {
    "name": "John Doe", "age": 30, "city": "New York"
}
# access dictionary values by keys
print(customers["name"])
print(customers["age"])

# add values
customers["email"] = "adf@gmai.com"
customers["age"] = 29
#print(customers)

for key, value in customers.items():
    print(key, ":", value)

def add_balance(customer, amount):
    if "balance" not in customer:
        customer["balance"] = 0
    customer["balance"] += amount
    return customer 

customer = {"name": "Alice", "balance": 0}
updatedCus = add_balance(customer, 100)

print("Updated balance:", updatedCus)