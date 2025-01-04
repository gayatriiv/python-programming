import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    age = age_entry.get()
    address = address_entry.get()
    
    # Display the entered values in a message box
    messagebox.showinfo("Registration Info", f"Name: {name}\nAge: {age}\nAddress: {address}")

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Create and place the Name label and entry
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

# Create and place the Age label and entry
age_label = tk.Label(root, text="Age:")
age_label.grid(row=1, column=0, padx=10, pady=10)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=10)

# Create and place the Address label and entry
address_label = tk.Label(root, text="Address:")
address_label.grid(row=2, column=0, padx=10, pady=10)
address_entry = tk.Entry(root)
address_entry.grid(row=2, column=1, padx=10, pady=10)

# Create and place the Submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=3, columnspan=2, pady=10)

# Start the GUI event loop
root.mainloop()

