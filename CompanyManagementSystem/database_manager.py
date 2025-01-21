import sqlite3

DB_FILE = "product_transactions.db"

def setup_database():
    """Set up the database and create necessary tables."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product TEXT,
            quantity INTEGER,
            rate REAL,
            total REAL,
            bought_sold TEXT,
            client_name TEXT,
            date_time TEXT,
            payment_status TEXT
        )
    """)

    # Create `customers` table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            contact_number TEXT NOT NULL,
            address TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stock (
            product TEXT PRIMARY KEY,
            quantity INTEGER NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS suppliers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            contact_number TEXT NOT NULL,
            address TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

def save_transaction(product, quantity, rate, client_name):
    """Save a transaction to the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Calculate product quantity (quantity * rate)
    total = quantity * rate
    from datetime import datetime
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bought_sold = "Sold"
    payment_status = "Pending"

    # Insert transaction into the database
    cursor.execute("""
        INSERT INTO transactions (product, quantity, rate,total, bought_sold, client_name, date_time, payment_status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (product, quantity, rate, total, bought_sold, client_name, date_time, payment_status))

    conn.commit()
    conn.close()

def save_purchase_entry(product, quantity, rate, client_name):
    """Save a transaction to the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Calculate product quantity (quantity * rate)
    total = quantity * rate
    from datetime import datetime
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bought_sold = "Bought"
    payment_status = "Pending"

    # Insert transaction into the database
    cursor.execute("""
        INSERT INTO transactions (product, quantity, rate,total, bought_sold, client_name, date_time, payment_status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (product, quantity, rate, total, bought_sold, client_name, date_time, payment_status))

    conn.commit()
    conn.close()

def fetch_customers():
    """Fetch all customers from the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM customers")
    customers = [row[0] for row in cursor.fetchall()]
    conn.close()
    return customers

def fetch_supplier():
    """Fetch all suppliers from the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM suppliers")
    suppliers = [row[0] for row in cursor.fetchall()]
    conn.close()
    return suppliers

 

def add_customer(name, contact_number, address):
    """Add a customer into the Database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    try:
        # Insert customer details into the database
        cursor.execute("""
            INSERT INTO customers (name, contact_number, address)
            VALUES (?, ?, ?)
        """, (name, contact_number, address))
        
        # Commit the transaction
        conn.commit()
        print(f"Customer '{name}' added successfully!")
    except sqlite3.IntegrityError as e:
        # Handle duplicate entries (e.g., unique constraint on name)
        print(f"Error: {e}. Customer with the name '{name}' already exists.")
        raise Exception("Customer with this name already exists.")
    except Exception as e:
        # Handle other errors
        print(f"An error occurred: {e}")
        raise
    finally:
        # Close the connection
        conn.close()

def add_supplier(name, contact_number, address):
    """Add a supplier into the Database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    try:
        # Insert customer details into the database
        cursor.execute("""
            INSERT INTO suppliers (name, contact_number, address)
            VALUES (?, ?, ?)
        """, (name, contact_number, address))
        
        # Commit the transaction
        conn.commit()
        print(f"Supplier '{name}' added successfully!")
    except sqlite3.IntegrityError as e:
        # Handle duplicate entries (e.g., unique constraint on name)
        print(f"Error: {e}. Supplier with the name '{name}' already exists.")
        raise Exception("Supplier with this name already exists.")
    except Exception as e:
        # Handle other errors
        print(f"An error occurred: {e}")
        raise
    finally:
        # Close the connection
        conn.close()

def delete_customer(name):
    """Delete a customer from the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM customers WHERE name = ?", (name,))
    conn.commit()
    conn.close()

def fetch_transactions_by_customer(customer_name):
    """Fetch all transactions for a specific customer."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, product, quantity, rate, total, date_time, payment_status
        FROM transactions
        WHERE client_name = ?
    """, (customer_name,))
    transactions = cursor.fetchall()
    conn.close()
    return transactions

def add_stock(product, quantity):
    """Add or update stock for a product."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Check if the product exists in stock
    cursor.execute("SELECT quantity FROM stock WHERE product = ?", (product,))
    result = cursor.fetchone()
    
    if result:
        # Update the quantity if the product exists
        new_quantity = result[0] + quantity
        cursor.execute("UPDATE stock SET quantity = ? WHERE product = ?", (new_quantity, product))
    else:
        # Insert a new product with its quantity
        cursor.execute("INSERT INTO stock (product, quantity) VALUES (?, ?)", (product, quantity))
    
    conn.commit()
    conn.close()

def deduct_stock(product, quantity):
    """Deduct stock for a product after a transaction."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Check the current stock
    cursor.execute("SELECT quantity FROM stock WHERE product = ?", (product,))
    result = cursor.fetchone()
    
    if result:
        current_quantity = result[0]
        if current_quantity >= quantity:
            # Deduct the quantity
            new_quantity = current_quantity - quantity
            cursor.execute("UPDATE stock SET quantity = ? WHERE product = ?", (new_quantity, product))
        else:
            conn.close()
            raise ValueError(f"Not enough stock for {product}. Available: {current_quantity}, Required: {quantity}.")
    else:
        conn.close()
        raise ValueError(f"Product {product} not found in stock.")
    
    conn.commit()
    conn.close()

def fetch_stock():
    """Fetch stock details for all products."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stock")
    stock_data = cursor.fetchall()
    conn.close()
    return stock_data
