import tkinter as tk
from tkinter import ttk, messagebox
from database_manager import fetch_transactions_by_customer, fetch_customers

def show_customer_history():
    """Show a basic customer history window."""

    def show_history():
        """Fetch and display the customer's transaction history."""
        selected_customer = customer_combobox.get().strip()

        if not selected_customer:
            messagebox.showerror("Error", "Please select a customer.")
            return

        # Fetch transactions for the selected customer
        transactions = fetch_transactions_by_customer(selected_customer)

        # Clear the treeview before adding new data
        for row in history_tree.get_children():
            history_tree.delete(row)

        if transactions:
            for transaction in transactions:
                history_tree.insert("", "end", values=transaction)
        else:
            messagebox.showinfo("No Data", f"No transactions found for {selected_customer}.")

    # Create the main window
    root = tk.Tk()
    root.title("Customer History")
    root.geometry("600x400")

    # Dropdown for customer selection
    tk.Label(root, text="Select Customer:", font=("Arial", 12)).pack(pady=5)
    customer_combobox = ttk.Combobox(root, state="readonly")
    customer_combobox.pack(pady=5)

    # Populate dropdown with customer names
    customers = fetch_customers()  # Fetch customer names from the database
    customer_combobox["values"] = customers

    # Button to show history
    tk.Button(root, text="Show History", command=show_history, bg="blue", fg="white").pack(pady=10)

    # Table to display transactions
    columns = ("ID", "Product", "Quantity", "Rate", "Total", "Date/Time", "Payment Status")
    history_tree = ttk.Treeview(root, columns=columns, show="headings")
    history_tree.pack(fill="both", expand=True)

    # Configure table headings
    for col in columns:
        history_tree.heading(col, text=col)
        history_tree.column(col, width=100)

    # Run the application
    root.mainloop()
