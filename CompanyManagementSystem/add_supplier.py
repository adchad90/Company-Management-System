import tkinter as tk
from tkinter import messagebox
from database_manager import add_supplier

def add_supplier_popup():
    """Create a popup window to add a new supplier."""
    def handle_save():
        """Handle the Save button click."""
        name = name_entry.get().strip()
        contact_number = contact_entry.get().strip()
        address = address_entry.get().strip()

        # Validate input
        if not name or not contact_number or not address:
            messagebox.showerror("Missing Data", "Please fill in all fields.")
            return
        
        if not contact_number.isdigit():
            messagebox.showerror("Invalid Contact Number", "Contact number must be numeric.")
            return

        try:
            # Save supplier details using the save_supplier function
            add_supplier(name, contact_number, address)
            messagebox.showinfo("Success", f"supplier '{name}' added successfully!")
            popup.destroy()  # Close the popup window
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Create the popup window
    popup = tk.Toplevel()
    popup.title("Add supplier")
    popup.geometry("400x300")
    popup.resizable(False, False)

    # Labels and Entry fields for supplier details
    tk.Label(popup, text="supplier Name:", font=("Arial", 12)).pack(pady=10)
    name_entry = tk.Entry(popup, width=30)
    name_entry.pack(pady=5)

    tk.Label(popup, text="Contact Number:", font=("Arial", 12)).pack(pady=10)
    contact_entry = tk.Entry(popup, width=30)
    contact_entry.pack(pady=5)

    tk.Label(popup, text="Address:", font=("Arial", 12)).pack(pady=10)
    address_entry = tk.Entry(popup, width=30)
    address_entry.pack(pady=5)

    # Save Button
    save_button = tk.Button(popup, text="Save", command=handle_save, bg="green", fg="white", font=("Arial", 12))
    save_button.pack(pady=20)

# Example: Call this function to test the popup
# if __name__ == "__main__":
#     root = tk.Tk()
#     root.withdraw()  # Hide the main window
#     add_supplier_popup()
#     root.mainloop()

