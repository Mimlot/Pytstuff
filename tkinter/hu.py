import tkinter as tk
from tkinter import ttk

def add_to_treeview():
    # Get the data from the entry widget
    input_data = entry.get()
    
    if input_data.strip():  # Check if the input is not empty
        treeview.insert("", "end", values=(input_data,))
        entry.delete(0, tk.END)  # Clear the entry widget after adding the data
    else:
        print("Entry is empty!")  # Debug message

# Create the main window
root = tk.Tk()
root.title("Tkinter Entry to Treeview")

# Create and place the Entry widget
entry_label = tk.Label(root, text="Enter Data:")
entry_label.pack(pady=5)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Create and place the Button widget
add_button = tk.Button(root, text="Add to Treeview", command=add_to_treeview)
add_button.pack(pady=5)

# Create and place the Treeview widget
columns = ("Data",)
treeview = ttk.Treeview(root, columns=columns, show="headings", height=8)
treeview.heading("Data", text="Data")
treeview.pack(pady=10)

# Start the main event loop
root.mainloop()
