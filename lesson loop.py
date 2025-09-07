for i in range(6):
    if i == 4 or i == 3:
        continue
    print(i)



# import pandas as pd

# transactions = [
#     {"Name": "Alice", "Amount": 50, "Type": "Deposit"},
#     {"Name": "Bob", "Amount": 30, "Type": "Deposit"},
#     {"Name": "Alice", "Amount": -20, "Type": "Withdraw"},
#     {"Name": "Bob", "Amount": -10, "Type": "Withdraw"},
#     {"Name": "Alice", "Amount": 70, "Type": "Deposit"},
# ]
# balance = 0 
# for t in transactions:
#     balance += t.get("Amount", 0)
#     t["Balance"] = balance

# print(t)
# table= [(t["Name"], t["Amount"],t["Balance"] ) for t in transactions]

# df = pd.DataFrame(table, columns=["Name", "Amount","Balance"])
# print(df)