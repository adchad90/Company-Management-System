import sqlite3

DB_FILE = "product_transactions.db"

# Connect to the database
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Check the schema of the 'transactions' table
cursor.execute("PRAGMA table_info(transactions)")
schema = cursor.fetchall()

# Print the schema
for column in schema:
    print(column)

conn.close()
