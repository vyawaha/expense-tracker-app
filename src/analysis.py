import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cleaned_expenses.csv")

# CATEGORY ANALYSIS
cat = df.groupby("Category")["Amount"].sum()

plt.figure()
cat.plot(kind="bar")
plt.title("Category Wise Spending")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# MONTHLY TREND
month = df.groupby("Month")["Amount"].sum()

plt.figure()
month.plot(kind="line", marker="o")
plt.title("Monthly Spending Trend")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# PIE CHART
expense = df[df["Type"] == "Expense"].groupby("Category")["Amount"].sum()

plt.figure()
expense.plot(kind="pie", autopct="%1.1f%%")
plt.title("Expense Distribution")
plt.ylabel("")
plt.show()

print("📊 Analysis complete")