import tkinter as tk
from tkinter import ttk
import pyodbc as odbc

# Database connection
con_str = (
    'DRIVER={SQL Server};'
    'SERVER=DESKTOP-QB8L5VP\\SQLEXPRESS;'
    'DATABASE=Test;'
)
conn = odbc.connect(con_str)
cursor = conn.cursor()

# Fetch data from database
def fetch_data():
    cursor.execute("SELECT * FROM Test.dbo.SP")
    rows = cursor.fetchall()
    # Clear the treeview before inserting new data
    for item in table.get_children():
        table.delete(item)
    # Insert each row into the Treeview
    for row in rows:
        table.insert("", "end", values=row)

# GUI setup
root = tk.Tk()
root.title("Quản lý sản phẩm")
root.geometry("1280x720")

def comm():
    input_data = e1.get()
    input_data2 = e2.get()
    input_data3 = e3.get()
    if input_data.strip():
        table.insert("", "end", values=(input_data, input_data2, input_data3))
        e1.delete(0, tk.END)
        e2.delete(0, tk.END)
        e3.delete(0, tk.END)
    else:
        print("Vui lòng nhập dữ liệu!")

# Input fields
lb = tk.Label(root, text="Tên")
e1 = tk.Entry(root)
e1.grid(row=1)
e2 = tk.Entry(root)
e2.grid(row=2)
e3 = tk.Entry(root)
e3.grid(row=3)
btn1 = tk.Button(root, text="Real", command=comm)
btn1.grid(row=4)

# Treeview
table = ttk.Treeview(root, columns=('first', 'mid', 'tail'), show='headings')
table.heading("first", text="Tên")
table.heading("mid", text="Địa chỉ")
table.heading("tail", text="Số tầng")
table.grid(row=5)

# Fetch data button
btn_fetch = tk.Button(root, text="Fetch Data", command=fetch_data)
btn_fetch.grid(row=6)

root.mainloop()
