from cx_Freeze import setup, Executable
import sys

# Include additional files like icons, database, or other assets
include_files = [
    'logo.ico',  # Replace with your actual icon file
    'database.db',  # Example database file (add your actual files)
    'add_supplier.py',
    'addCustomer.py',
    'current_stock.py',
    'customer_history.py',
    'database_manager.py',
    'eway_bill.py',
    'fetchdb.py'
]

# List any excluded modules (if needed)
excludes = []

# List additional packages used in your project
packages = []

# Define the base for the executable
base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Suppress the console for GUI apps

# MSI Shortcut Table
shortcut_table = [
    (
        "DesktopShortcut",  # Shortcut name
        "DesktopFolder",  # Shortcut location
        "Aditya's Billing System",  # Shortcut display name
        "TARGETDIR",  # Location of the target
        "[TARGETDIR]main.exe",  # Path to the executable
        None,  # Arguments
        None,  # Description
        None,  # Hotkey
        None,  # Icon
        None,  # Icon index
        None,  # Working directory
        "TARGETDIR",  # Start in
    )
]

# MSI Data (to define shortcuts)
msi_data = {
    "Shortcut": shortcut_table
}

# MSI Build Options
bdist_msi_options = {
    "data": msi_data,
}

# Setup Configuration
setup(
    name="Company Management",
    version="0.1",
    description="Billing System beta",
    author="Aditya Chavan, Pratham Bhamare",
    options={
        'build_exe': {
            'include_files': include_files,  # Files to include
        },
        'bdist_msi': bdist_msi_options,  # MSI options
    },
    executables=[
        Executable(
            script="finalmain.py",  # Main script of your application
            base=base,
            icon="icon.ico",  # Application icon
        )
    ]
)
