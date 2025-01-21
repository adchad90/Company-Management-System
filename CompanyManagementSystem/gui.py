import tkinter as tk
from tkinter import Toplevel


# Function to create a new window
def open_window(title):
    new_window = Toplevel()
    new_window.title(title)
    new_window.geometry("1000x600")
    new_window.config(bg="#2E2E2E")  # Dark mode background
    tk.Label(
        new_window,
        text=f"{title} Page",
        font=("Arial", 16),
        fg="#FFFFFF",
        bg="#2E2E2E",
        pady=20,
    ).pack()

    # Example placeholder content
    tk.Label(
        new_window,
        text=f"Details for {title} will go here...",
        font=("Arial", 12),
        fg="#AAAAAA",
        bg="#2E2E2E",
    ).pack()


# Main application window
root = tk.Tk()
root.title("Business Management System")
root.geometry("600x500")
root.config(bg="#1C1C1C")  # Dark background color

# Header
header = tk.Label(
    root,
    text="Business Management System",
    font=("Arial", 20, "bold"),
    fg="#FFFFFF",
    bg="#1C1C1C",
    pady=20,
)
header.grid(row=0, column=0, columnspan=3)

# Button details
buttons = [
    "Current Stock", "Generate Invoice", "Generate Bill", "Customer History",
    "Purchase Entry", "Product Details", "Purchase Order", "Quotation",
    "E-Way Bills", "Supplier Details", "Transaction", "Daily Rates"
]

# Button styles
button_color = "#3A3A3A"
hover_color = "#555555"
text_color = "#FFFFFF"

# Function to change button color on hover
def on_enter(e):
    e.widget.config(bg=hover_color)

def on_leave(e):
    e.widget.config(bg=button_color)


# Create buttons dynamically with grid layout
for i, name in enumerate(buttons):
    btn = tk.Button(
        root,
        text=name,
        font=("Arial", 12),
        bg=button_color,
        fg=text_color,
        activebackground=hover_color,
        activeforeground=text_color,
        width=20,
        height=2,
        command=lambda n=name: open_window(n),
        relief="flat"
    )
    btn.grid(row=1 + i // 3, column=i % 3, padx=10, pady=10)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

# Run the application
root.mainloop()
