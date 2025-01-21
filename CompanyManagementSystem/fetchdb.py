import sqlite3

DB_FILE = "product_transactions.db"

def fetch_transactions():
    """Fetch all transactions from the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Execute the SELECT query
    cursor.execute("SELECT * FROM transactions")
    rows = cursor.fetchall()

    # Print each transaction
    for row in rows:
        print(row)

    cursor.execute("SELECT * FROM customers")
    rows = cursor.fetchall()

    # Print each transaction
    #for row in rows:
        #print(row)
    cursor.execute("SELECT * FROM suppliers")
    rows = cursor.fetchall()

    #for row in rows:
        #print(row)

    conn.close()

# Call the function
fetch_transactions()
