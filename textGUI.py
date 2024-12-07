import tkinter as tk
from tkinter import ttk

def submit():
    print("Đăng ký thành công!")

def reset():
    fullname_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    gender_var.set('')
    course_var.set('')
    payment_var.set('')
    for day_var in day_vars:
        day_var.set(0)


root = tk.Tk()
root.title("Đăng ký khóa học")

info_frame = tk.LabelFrame(root, text="THÔNG TIN HỌC VIÊN", padx=10, pady=10)
info_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

tk.Label(info_frame, text="Họ và Tên:").grid(row=0, column=0, padx=5, pady=5)
fullname_entry = tk.Entry(info_frame)
fullname_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(info_frame, text="Giới tính:").grid(row=1, column=0, padx=5, pady=5)
gender_var = tk.StringVar()
gender_var.set("Nam") 
tk.Radiobutton(info_frame, text="Nam", variable=gender_var, value="Nam").grid(row=1, column=1, padx=5, pady=5)
tk.Radiobutton(info_frame, text="Nữ", variable=gender_var, value="Nữ").grid(row=1, column=2, padx=5, pady=5)

tk.Label(info_frame, text="Email:").grid(row=2, column=0, padx=5, pady=5)
email_entry = tk.Entry(info_frame)
email_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(info_frame, text="Điện thoại:").grid(row=3, column=0, padx=5, pady=5)
phone_entry = tk.Entry(info_frame)
phone_entry.grid(row=3, column=1, padx=5, pady=5)


course_frame = tk.LabelFrame(root, text="THÔNG TIN KHÓA HỌC", padx=10, pady=10)
course_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

tk.Label(course_frame, text="Chọn khóa học:").grid(row=0, column=0, padx=5, pady=5)
course_var = tk.StringVar()
course_combobox = ttk.Combobox(course_frame, textvariable=course_var)
course_combobox['values'] = ("Khóa học 1", "Khóa học 2", "Khóa học 3")
course_combobox.grid(row=0, column=1, padx=5, pady=5)


days_frame = tk.LabelFrame(course_frame, text="Chọn ngày học", padx=10, pady=10)
days_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

day_vars = []
days = ["Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7"]
for i, day in enumerate(days):
    var = tk.IntVar()
    day_vars.append(var)
    tk.Checkbutton(days_frame, text=day, variable=var).grid(row=i % 3, column=i // 3, sticky="w", padx=5, pady=2)

tk.Label(course_frame, text="Phương thức thanh toán:").grid(row=2, column=0, padx=5, pady=5)
payment_var = tk.StringVar()
payment_var.set("Chuyển khoản")
tk.Radiobutton(course_frame, text="Chuyển khoản", variable=payment_var, value="Chuyển khoản").grid(row=2, column=1, padx=5, pady=5)
tk.Radiobutton(course_frame, text="Tiền mặt", variable=payment_var, value="Tiền mặt").grid(row=2, column=2, padx=5, pady=5)


button_frame = tk.Frame(root)
button_frame.grid(row=1, columnspan=2, pady=10)

tk.Button(button_frame, text="ĐĂNG KÝ", command=submit).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="NHẬP LẠI", command=reset).grid(row=0, column=1, padx=10)


root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)


root.mainloop()