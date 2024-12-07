import tkinter as tk
from tkinter import ttk, messagebox

def submit_data():
    # Collect data from the form
    data = {
        "MaHoso": entry_mahoso.get(),
        "LoaiHoso": combo_loaihoso.get(),
        "NgayXuat": entry_ngayxuat.get(),
        "MaLoHang": entry_malohang.get(),
        "TenLoHang": entry_tenlohang.get(),
        "SoLuong": entry_soluong.get(),
        "MaKho": entry_makho.get(),
        "TinhTrang": combo_tinhtrang.get(),
    }

    # Validate required fields
    missing_fields = [k for k, v in data.items() if not v]
    if missing_fields:
        messagebox.showerror("Lỗi", f"Các trường sau không được bỏ trống: {', '.join(missing_fields)}")
        return

    # Simulate saving data to a database
    messagebox.showinfo("Thành công", "Dữ liệu xuất hàng đã được lưu thành công!")
    root.destroy()

# Create the main application window
root = tk.Tk()
root.title("Xuất Hàng Khỏi Kho Hải Quan")
root.geometry("500x600")

# Header
header = tk.Label(root, text="Xuất Hàng Khỏi Kho Hải Quan", font=("Arial", 16), pady=10)
header.pack()

# Create the form
form_frame = tk.Frame(root, padx=10, pady=10)
form_frame.pack(fill=tk.BOTH, expand=True)

# Fields
fields = [
    ("Mã Hồ Sơ", "entry_mahoso"),
    ("Loại Hồ Sơ", "combo_loaihoso"),
    ("Ngày Xuất (YYYY-MM-DD)", "entry_ngayxuat"),
    ("Mã Lô Hàng", "entry_malohang"),
    ("Tên Lô Hàng", "entry_tenlohang"),
    ("Số Lượng Hàng", "entry_soluong"),
    ("Mã Kho Ngoại Quan", "entry_makho"),
    ("Tình Trạng Hàng Hóa", "combo_tinhtrang"),
]

entries = {}
for i, (label_text, var_name) in enumerate(fields):
    label = tk.Label(form_frame, text=label_text, anchor="w", padx=5, pady=5)
    label.grid(row=i, column=0, sticky="w")

    if "combo" in var_name:
        # Combo box for specific fields
        combo = ttk.Combobox(form_frame, state="readonly")
        if var_name == "combo_loaihoso":
            combo["values"] = ["Xuất kho"]
        elif var_name == "combo_tinhtrang":
            combo["values"] = ["Tốt", "Hỏng hóc", "Khác"]
        combo.grid(row=i, column=1, padx=5, pady=5, sticky="we")
        entries[var_name] = combo
    else:
        entry = tk.Entry(form_frame)
        entry.grid(row=i, column=1, padx=5, pady=5, sticky="we")
        entries[var_name] = entry

# Map entries to variables
entry_mahoso = entries["entry_mahoso"]
combo_loaihoso = entries["combo_loaihoso"]
entry_ngayxuat = entries["entry_ngayxuat"]
entry_malohang = entries["entry_malohang"]
entry_tenlohang = entries["entry_tenlohang"]
entry_soluong = entries["entry_soluong"]
entry_makho = entries["entry_makho"]
combo_tinhtrang = entries["combo_tinhtrang"]

# Buttons
btn_frame = tk.Frame(root, pady=10)
btn_frame.pack(fill=tk.X)

submit_btn = tk.Button(btn_frame, text="Lưu Dữ Liệu", command=submit_data, bg="green", fg="white", padx=10, pady=5)
submit_btn.pack(side=tk.LEFT, padx=10)

cancel_btn = tk.Button(btn_frame, text="Hủy Bỏ", command=root.destroy, bg="red", fg="white", padx=10, pady=5)
cancel_btn.pack(side=tk.RIGHT, padx=10)

# Start the main loop
root.mainloop()
