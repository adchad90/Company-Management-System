import tkinter as tk
from tkinter import messagebox
import sqlite3

DB_FILE = "product_transactions.db"

def fetch_current_stock():
    """Fetch the current stock levels from the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT product, quantity FROM stock")
    stock_data = cursor.fetchall()
    conn.close()

    return stock_data

def open_current_stock_page():
    """Open the Current Stock page."""
    stock_window = tk.Toplevel()
    stock_window.title("Current Stock")
    stock_window.geometry("400x300")

    # Header
    tk.Label(stock_window, text="Current Stock Levels", font=("Arial", 16, "bold")).pack(pady=10)

    # Frame for stock information
    stock_frame = tk.Frame(stock_window)
    stock_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Fetch stock data
    stock_data = fetch_current_stock()

    if not stock_data:
        tk.Label(stock_frame, text="No stock data available.", font=("Arial", 12), fg="red").pack(pady=20)
    else:
        # Display stock data
        for product, quantity in stock_data:
            tk.Label(stock_frame, text=f"{product}: {quantity} units", font=("Arial", 12)).pack(anchor="w", pady=5)

    # Close Button
    tk.Button(stock_window, text="Close", command=stock_window.destroy, bg="red", fg="white").pack(pady=10)

