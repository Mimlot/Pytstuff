import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Quản lý khóa học")


root_lable = ttk.Label(root, text="CHƯƠNG TRÌNH QUẢN LÝ THÔNG TIN ĐĂNG KÝ KHÓA HỌC")
root_lable.grid(row=0, column=0, columnspan=2, pady=10)


form_frame = ttk.LabelFrame(root, text="THÔNG TIN HỌC VIÊN", padding=(10, 10))
form_frame.grid(row=1, column=0, padx=20, pady=20, sticky="ew")


name_label = ttk.Label(form_frame, text="Tên:")
name_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
name_entry = ttk.Entry(form_frame, width=30)
name_entry.grid(row=0, column=1, padx=5, pady=5)


gender_label = ttk.Label(form_frame, text="Giới tính:")
gender_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
gender_var = tk.StringVar()
male_radio = ttk.Radiobutton(form_frame, text="Nam", variable=gender_var, value="Nam")
male_radio.grid(row=1, column=1, sticky="w", padx=5)
female_radio = ttk.Radiobutton(form_frame, text="Nữ", variable=gender_var, value="Nu")
female_radio.grid(row=1, column=1, sticky="e", padx=5)


email_label = ttk.Label(form_frame, text="Email:")
email_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
email_entry = ttk.Entry(form_frame, width=30)
email_entry.grid(row=2, column=1, padx=5, pady=5)


phone_label = ttk.Label(form_frame, text="Số điện thoại:")
phone_label.grid(row=3, column=0, sticky="w", padx=5, pady=5)
phone_entry = ttk.Entry(form_frame, width=30)
phone_entry.grid(row=3, column=1, padx=5, pady=5)


dk_btn = ttk.Button(root, text="Đăng ký")
dk_btn.grid(row=2, column=0, sticky="e", padx=5, pady=5)

reset_btn = ttk.Button(root, text="Nhập lại")
reset_btn.grid(row=2, column=0, sticky="w", padx=5, pady=5)


course_frame = ttk.LabelFrame(root, text="THÔNG TIN KHÓA HỌC", padding=(10, 10))
course_frame.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

course_label = ttk.Label(course_frame, text="Chọn khóa học:")
course_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
course_options = ["CNTT", "Sư phạm tin", "KHMT"]
course_var = tk.StringVar()
course_dropdown = ttk.Combobox(course_frame, textvariable=course_var, values=course_options, width=27)
course_dropdown.grid(row=0, column=1, padx=5, pady=5)
course_dropdown.set("")


day_label = ttk.Label(course_frame, text="Chọn ngày học")
day_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
day_var = tk.StringVar()
days = ["Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7", "Chủ nhật",]
for i, day in enumerate(days):
    day_radio = ttk.Radiobutton(course_frame, text=day, variable=day_var, value=day)
    day_radio.grid(row=i+1, column=1, sticky="w", padx=5)


pay_method = tk.Label(course_frame, text="Chọn phương thức thanh toán:")
pay_method.grid(row=8, column=0, sticky="w", padx=5, pady=5)
money_var = tk.StringVar()
card_radio = ttk.Radiobutton(course_frame, text="Chuyển khoản", variable=money_var, value="the")
card_radio.grid(row=9, column=0, sticky="w", padx=5)
cash_radio = ttk.Radiobutton(course_frame, text="Tiền mặt", variable=money_var, value="cash")
cash_radio.grid(row=9, column=1, sticky="e", padx=5)

root.mainloop()
