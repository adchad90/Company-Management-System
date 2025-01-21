import tkinter as tk
from tkinter import messagebox, ttk  # Importing ttk for combobox
from database_manager import save_purchase_entry, fetch_supplier
from datetime import datetime
from database_manager import add_stock

# Product details from product_details.py
PRODUCTS = {
    "Sulphuric Acid": 50.0,  # Rate per unit
    "Nitric Acid": 60.0,  # Rate per unit
    # Add more products with their rates here
}

def open_purchase_entry():
    """Open the Purchase entry window."""
    def update_rate(event):
        """Update the rate field based on the selected product."""
        selected_product = product_combobox.get()
        if selected_product in PRODUCTS:
            rate_entry.delete(0, tk.END)  # Clear the current rate
            rate_entry.insert(0, str(PRODUCTS[selected_product]))  # Set the predefined rate

    def generate_txt_purchase_entry(client_name, product, quantity, rate, total):
        """Generate a TXT purchase entry."""
    # Format the date for the file name
        current_date = datetime.now().strftime("%Y-%m-%d")
    # Replace spaces with underscores in the client name for a valid file name
        sanitized_name = client_name.replace(" ", "_")
        file_name = f"Bills/purchase_{sanitized_name}_{current_date}.txt"

    # Write to the file with UTF-8 encoding
        with open(file_name, "w", encoding="utf-8") as file:
            file.write("********** Purchase entry **********\n")
            file.write("\n")
            file.write(f"Supplier Name: {client_name}\n")
            file.write(f"Product: {product}\n")
            file.write(f"Quantity: {quantity}\n")
            file.write(f"Rate (per unit): ₹{rate:.2f}\n")
            file.write(f"Total: ₹{total:.2f}\n")
            file.write("\n")
            file.write("******************************\n")
            file.write("Thank you for your purchase!\n")

    # Notify the user
        messagebox.showinfo("Success", f"Invoice saved as {file_name}")


    def handle_submit():
        """Handle the Purchase entry button click."""
        # Get user input
        client_name = supplier_combobox.get().strip()
        product = product_combobox.get().strip()
        try:
            quantity = int(quantity_entry.get().strip())
            rate = float(rate_entry.get().strip())
        except ValueError:
            messagebox.showerror("Invalid Input", "Quantity must be an integer, and Rate must be a number.")
            return

        if not client_name or not product:
            messagebox.showerror("Missing Data", "Please fill in all fields.")
            return

        #add stock
        try:
            add_stock(product, quantity)
        except ValueError as e:
            messagebox.showerror("Stock Error", str(e))
            return
        
        # Calculate total
        total = quantity * rate

        # Save to database
        save_purchase_entry(product, quantity, rate, client_name)

        # Generate the Purchase entry
        generate_txt_purchase_entry(client_name, product, quantity, rate, total)

        # Close the Purchase entry window after submission
        invoice_window.destroy()

    # Fetch supplier names from the database
    supplier_names = fetch_supplier()

    # Create a popup window
    invoice_window = tk.Toplevel()
    invoice_window.title("Purchase Entry")
    invoice_window.geometry("400x500")

    # Labels and Entry Fields
    tk.Label(invoice_window, text="supplier Name:").pack(pady=5)

    # Dropdown (Combobox) for supplier selection
    supplier_combobox = ttk.Combobox(invoice_window, values=supplier_names, state="readonly")
    supplier_combobox.pack(pady=5)

    tk.Label(invoice_window, text="Product Name:").pack(pady=5)

    # Dropdown (Combobox) for product selection
    product_combobox = ttk.Combobox(invoice_window, values=list(PRODUCTS.keys()), state="readonly")
    product_combobox.pack(pady=5)
    product_combobox.bind("<<ComboboxSelected>>", update_rate)  # Bind selection event to update rate

    tk.Label(invoice_window, text="Quantity:").pack(pady=5)
    quantity_entry = tk.Entry(invoice_window)
    quantity_entry.pack(pady=5)

    tk.Label(invoice_window, text="Rate (per unit):").pack(pady=5)
    rate_entry = tk.Entry(invoice_window)
    rate_entry.pack(pady=5)

    # Submit Button
    tk.Button(invoice_window, text="Generate Invoice", command=handle_submit, bg="green", fg="white").pack(pady=20)
