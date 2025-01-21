import tkinter as tk
import webbrowser

def open_eway_bill_website():
    """
    Redirect the user to the official e-way bill generation website.
    """
    webbrowser.open("https://docs.ewaybillgst.gov.in/")
    print("Redirecting to the e-way bill generation website.")