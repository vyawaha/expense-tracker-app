import pandas as pd

df = pd.read_csv("data/expenses.csv")

df.drop_duplicates(inplace=True)

df['Date'] = pd.to_datetime(df['Date'])
df['Category'] = df['Category'].str.title()
df['Type'] = df['Type'].str.title()

df['Month'] = df['Date'].dt.month_name()
df['Weekday'] = df['Date'].dt.day_name()

df.to_csv("data/cleaned_expenses.csv", index=False)

print("✅ Data cleaned successfully")