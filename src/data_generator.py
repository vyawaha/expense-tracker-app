import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

categories = ["Food", "Travel", "Rent", "Shopping", "Bills", "Entertainment", "Salary"]
types = ["Expense", "Income"]

start_date = datetime(2024, 1, 1)
data = []

for i in range(300):
    date = start_date + timedelta(days=i)
    category = random.choice(categories)
    txn_type = random.choice(types)

    amount = random.randint(200, 5000)

    if txn_type == "Income":
        amount *= 5

    data.append([date, category, txn_type, amount])

df = pd.DataFrame(data, columns=["Date", "Category", "Type", "Amount"])
df.to_csv("data/expenses.csv", index=False)

print("✅ Synthetic dataset created")