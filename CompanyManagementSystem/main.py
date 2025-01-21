import tkinter as tk
from tkinter import messagebox
from product_details import show_product_details
from database_manager import setup_database
from invoice_generator import open_invoice_generator
from addCustomer import add_customer_popup
from customer_history import show_customer_history
from current_stock import open_current_stock_page
from add_supplier import add_supplier_popup
from purchase_entry import open_purchase_entry
from eway_bill import open_eway_bill_website

# Ensure the database is set up
setup_database()

# Create the main window
root = tk.Tk()
root.title("Business Management System")
root.geometry("600x400")  # Adjusted size for the three-column layout
root.configure(bg="#f0f0f0")  # Light gray background

# Heading
header = tk.Label(
    root,
    text="Business Management System",
    font=("Arial", 18, "bold"),
    bg="#4CAF50",
    fg="white",
    pady=10,
)
header.pack(fill=tk.X)

# Main Frame to hold the three columns
main_frame = tk.Frame(root, bg="#f0f0f0", pady=10)
main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

# Function to create styled buttons
def create_button(parent, text, command, bg="#2196F3", fg="white"):
    return tk.Button(
        parent,
        text=text,
        command=command,
        font=("Arial", 12),
        bg=bg,
        fg=fg,
        relief=tk.RAISED,
        padx=10,
        pady=5,
        width=20,
    )

# Features Column
features_frame = tk.Frame(main_frame, bg="#f0f0f0")
features_frame.grid(row=0, column=0, padx=10, sticky="n")
tk.Label(features_frame, text="Features", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(anchor="w")
create_button(features_frame, "Generate Invoice", open_invoice_generator).pack(pady=5)
create_button(features_frame, "Customer History", show_customer_history).pack(pady=5)
create_button(features_frame, "Current Stock", open_current_stock_page).pack(pady=5)
create_button(features_frame, "Purchase Entry", open_purchase_entry).pack(pady=5)

# Management Column
management_frame = tk.Frame(main_frame, bg="#f0f0f0")
management_frame.grid(row=0, column=1, padx=10, sticky="n")
tk.Label(management_frame, text="Management", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(anchor="w")
create_button(management_frame, "Add Customer", add_customer_popup).pack(pady=5)
create_button(management_frame, "Add Supplier", add_supplier_popup).pack(pady=5)
create_button(management_frame, "Open Product Details", show_product_details).pack(pady=5)

# Utilities Column
utilities_frame = tk.Frame(main_frame, bg="#f0f0f0")
utilities_frame.grid(row=0, column=2, padx=10, sticky="n")
tk.Label(utilities_frame, text="Utilities", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(anchor="w")
create_button(utilities_frame, "Purchase Order", lambda: messagebox.showinfo("Feature", "Coming Soon!")).pack(pady=5)
create_button(utilities_frame, "Quotation", lambda: messagebox.showinfo("Feature", "Coming Soon!")).pack(pady=5)
create_button(utilities_frame, "E-Way Bills", command=open_eway_bill_website).pack()
create_button(utilities_frame, "Transaction", lambda: messagebox.showinfo("Feature", "Coming Soon!")).pack(pady=5)

# Footer
footer = tk.Label(
    root,
    text="© 2024 Business Management System",
    font=("Arial", 10),
    bg="#4CAF50",
    fg="white",
    pady=5,
)
footer.pack(fill=tk.X, side=tk.BOTTOM)

# Run the application
root.mainloop()
