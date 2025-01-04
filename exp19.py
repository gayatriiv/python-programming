import tkinter as tk
from tkinter import messagebox
import sqlite3

# Create or connect to the database
def init_db():
    conn = sqlite3.connect("feedback.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            feedback TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Function to save feedback to the database
def save_feedback():
    name = name_entry.get()
    feedback = feedback_entry.get("1.0", tk.END).strip() 
    
    if name and feedback:
        # Connect to the database and insert feedback
        conn = sqlite3.connect("feedback.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO feedback (name, feedback) VALUES (?, ?)", (name, feedback))
        conn.commit()
        conn.close()
        
        messagebox.showinfo("Success", "Feedback saved successfully!")
        name_entry.delete(0, tk.END)  
        feedback_entry.delete("1.0", tk.END)  
    else:
        messagebox.showerror("Error", "Please fill in both fields.")

# Initialize the database
init_db()

# Create the GUI window
window = tk.Tk()
window.title("Feedback Form")
window.geometry("400x300")

# Name Label and Entry
tk.Label(window, text="Name:").pack(pady=10)
name_entry = tk.Entry(window, width=40)
name_entry.pack(pady=5)

# Feedback Label and Text Area
tk.Label(window, text="Feedback:").pack(pady=10)
feedback_entry = tk.Text(window, width=40, height=5)
feedback_entry.pack(pady=5)

# Submit Button
submit_button = tk.Button(window, text="Submit", command=save_feedback)
submit_button.pack(pady=20)

# Start the GUI event loop
window.mainloop()
