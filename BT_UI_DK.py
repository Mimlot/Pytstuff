import tkinter as tk
from tkinter import messagebox


User_name = "admin"
password = "1234"


def check_login():
   
    username = e1.get()
    password = e2.get()
    
   
    if username == User_name and password == password:
        messagebox.showinfo("Đăng nhập thành công!")
        root.destroy()  
    else:
        messagebox.showerror("Đăng nhập thất bại", "Sai tên người dùng hoặc mật khẩu")


root = tk.Tk()
root.title("Ví dụ sử dụng Tkinter")
root.geometry("400x300")

label0 = tk.Label(root, text="DANG NHAP")
label0.grid(row=0, columnspan=2)

label = tk.Label(root, text="Tai khoan")
label.grid(row=1)

label2 = tk.Label(root, text="Mat khau")
label2.grid(row=2)

e1 = tk.Entry(root)
e1.grid(row=1, column=1)

e2 = tk.Entry(root, show="*")  
e2.grid(row=2, column=1)

button = tk.Button(root, text='Đăng nhập', command=check_login)
button.grid(row=3, columnspan=2)

root.mainloop()
