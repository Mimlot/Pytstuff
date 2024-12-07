import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title("Quản lý sản phẩm")
root.geometry("1280x720")

def comm():
    input_data = e1.get()
    input_data2 = e2.get()
    input_data3 = e3.get()
    if input_data.strip():
        table.insert("", "end", values=(input_data, input_data2, input_data3))
        e1.delete(0,tk.END)
        e2.delete(0,tk.END)
        e3.delete(0,tk.END)
    else:
        print("Vui long nhap du lieu!")



lb = tk.Label(root, text="Ten")
e1 = tk.Entry(root)
e1.grid(row=1)
e2 = tk.Entry(root)
e2.grid(row=2)
e3 = tk.Entry(root)
e3.grid(row=3)
btn1 = tk.Button(root,text="real", command=comm)
btn1.grid(row=4)

table = ttk.Treeview(root, columns=('first', 'mid', 'tail'), show='headings')
table.heading("first", text="Ten")
table.heading("mid",text="Dia chi")
table.heading("tail",text="so_tang")
table.grid(row=5)

root.mainloop()