import os

print("🚀 Running Expense Tracker Pipeline...\n")

os.system("python src/data_generator.py")
os.system("python src/preprocess.py")
os.system("python src/analysis.py")

print("\n✅ Project executed successfully!")