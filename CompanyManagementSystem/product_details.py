import tkinter as tk
from PIL import Image, ImageTk

def show_product_details():
    # Create a new Toplevel window
    details_window = tk.Toplevel()
    details_window.title("Product Details")
    details_window.geometry("800x600")
    details_window.configure(bg="white")

    # Sample product data
    products = [
        {
            "title": "Sulphuric Acid",
            "image": "sulphuric_acid.png",  # Update with correct image path
            "description": "A highly corrosive strong acid used in industries.",
            "uses": "Fertilizers, batteries, chemical manufacturing.",
            "rate": "₹50 per liter"
        },
        {
            "title": "Nitric Acid",
            "image": "nitric_acid.png",  # Update with correct image path
            "description": "A reactive acid for fertilizers and explosives.",
            "uses": "Ammonium nitrate production, etching metals.",
            "rate": "₹60 per liter"
        },
    ]

    # Function to create product cards
    def create_product_card(parent, product):
        card = tk.Frame(parent, bg="lightgray", relief=tk.RAISED, borderwidth=2, padx=10, pady=10)
        card.pack(fill=tk.X, padx=20, pady=10)

        # Load product image
        try:
            img = Image.open(product["image"]).resize((100, 100), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            img_label = tk.Label(card, image=img, bg="lightgray")
            img_label.image = img
            img_label.grid(row=0, column=0, rowspan=3, padx=10)
        except:
            img_label = tk.Label(card, text="Image\nUnavailable", bg="lightgray", width=12, height=6)
            img_label.grid(row=0, column=0, rowspan=3, padx=10)

        # Product details
        title = tk.Label(card, text=product["title"], font=("Arial", 14, "bold"), bg="lightgray")
        title.grid(row=0, column=1, sticky="w", padx=10)

        description = tk.Label(card, text=f"Description: {product['description']}", wraplength=400, bg="lightgray")
        description.grid(row=1, column=1, sticky="w", padx=10)

        uses = tk.Label(card, text=f"Uses: {product['uses']}", wraplength=400, bg="lightgray")
        uses.grid(row=2, column=1, sticky="w", padx=10)

        rate = tk.Label(card, text=f"Rate: {product['rate']}", font=("Arial", 12, "bold"), fg="green", bg="lightgray")
        rate.grid(row=0, column=2, sticky="e", padx=10)

    # Header
    header = tk.Label(details_window, text="Chemical Product Details", font=("Arial", 18, "bold"), bg="blue", fg="white", pady=10)
    header.pack(fill=tk.X)

    # Frame for products
    products_frame = tk.Frame(details_window, padx=10, pady=10)
    products_frame.pack(fill=tk.BOTH, expand=True)

    # Create cards for each product
    for product in products:
        create_product_card(products_frame, product)