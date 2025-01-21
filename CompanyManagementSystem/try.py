from database_manager import setup_database
from database_manager import add_stock
from database_manager import fetch_stock
from database_manager import deduct_stock

# Example usage
setup_database()

# Add initial stock
add_stock("Sulphuric Acid", 100)
add_stock("Nitric Acid", 50)

# View current stock
print("Current stock:", fetch_stock())

# Deduct stock after a transaction
try:
    deduct_stock("Sulphuric Acid", 10)
except ValueError as e:
    print(e)

# View stock after deduction
print("Updated stock:", fetch_stock())
