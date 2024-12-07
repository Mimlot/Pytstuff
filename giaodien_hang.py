import pyodbc  # Để kết nối cơ sở dữ liệu
import tkinter as tk  # Để tạo giao diện người dùng
from tkinter import ttk  # Các widget nâng cao như Combobox, Treeview
from tkinter import messagebox  # Để hiển thị hộp thoại thông báo lỗi/thành công
from decimal import Decimal # sử dụng thư viện decimal để dùng kiểu dữ liệu decimal

# Cửa sổ chính
root = tk.Tk()
root.title("QLSP - Quản Lý Sản Phẩm")
root.geometry("900x600")  # Kích thước lớn hơn cho dễ sử dụng

# Cấu hình lại lưới
root.grid_columnconfigure(0, weight=1)  # Cột 0 có thể thay đổi kích thước
root.grid_columnconfigure(1, weight=3)  # Cột 1 có thể thay đổi kích thước nhiều hơn
root.grid_columnconfigure(2, weight=1)  # Cột 2 có thể thay đổi kích thước
root.grid_rowconfigure(0, weight=1)  # Dòng 0 có thể thay đổi kích thước
root.grid_rowconfigure(1, weight=1)  # Dòng 1 có thể thay đổi kích thước

# Danh sách các loại sản phẩm
danh_sach = ["Vip", "Loại 1", "Loại 2"]

# Biến toàn cục cho các widget
entry_masp = None
entry_tensp = None
entry_trongL = None
cmb_loai = None

# Hàm kết nối cơ sở dữ liệu
def ketnoi_db():
    try:
        conn = pyodbc.connect('DRIVER={SQL Server};'
                              'SERVER=DESKTOP-QB8L5VP\SQLEXPRESS;'
                              'DATABASE=Test;'
                              )
        return conn
    except Exception as e:
        messagebox.showerror("Lỗi", f"Kết nối cơ sở dữ liệu thất bại: {e}")
        return None

# Hàm làm mới Treeview sau khi thay đổi
def hienthiTree():
    # Xóa tất cả dữ liệu hiện tại trong Treeview
    for item in tree.get_children():
        tree.delete(item)

    # Truy vấn cơ sở dữ liệu để lấy tất cả sản phẩm
    conn = ketnoi_db()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM SP")
        rows = cursor.fetchall()

        # Thêm dữ liệu vào Treeview
        for row in rows:
            # Chuyển đổi Decimal thành chuỗi
            row_data = list(row)
            row_data[2] = float(row_data[2]) if isinstance(row_data[2], Decimal) else row_data[2]  # Chuyển trọng lượng
            tree.insert("", "end", values=row_data)

    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi khi lấy dữ liệu: {e}")
    finally:
        conn.close()


# Hàm tạo giao diện quản lý sản phẩm
def giaodienQL():
    global entry_masp, entry_tensp, entry_trongL, cmb_loai

    label_nhan = tk.Label(root, text="THÔNG TIN SẢN PHẨM", font=("Arial", 16, "bold"))
    label_nhan.grid(column=1, row=0, pady=10)

    # Tạo nhãn và trường nhập liệu
    label_masp = tk.Label(root, text="Mã Sản phẩm:", font=("Arial", 12))
    label_masp.grid(column=0, row=1, padx=10, pady=10)
    entry_masp = tk.Entry(root, font=("Arial", 12))
    entry_masp.grid(column=1, row=1, padx=10, pady=10)

    label_tensp = tk.Label(root, text="Tên sản phẩm:", font=("Arial", 12))
    label_tensp.grid(column=0, row=2, padx=10, pady=10)
    entry_tensp = tk.Entry(root, font=("Arial", 12))
    entry_tensp.grid(column=1, row=2, padx=10, pady=10)

    label_trongL = tk.Label(root, text="Trọng lượng:", font=("Arial", 12))
    label_trongL.grid(column=0, row=3, padx=10, pady=10)
    entry_trongL = tk.Entry(root, font=("Arial", 12))
    entry_trongL.grid(column=1, row=3, padx=10, pady=10)

    # Tạo Combobox cho loại sản phẩm
    label_loai = tk.Label(root, text="Loại:", font=("Arial", 12))
    label_loai.grid(column=0, row=4, padx=10, pady=10)
    cmb_loai = ttk.Combobox(root, values=['vip',"Loại 1","Loại 2", "Loại 3", 'đặc biêt'], state="readonly", font=("Arial", 12))
    cmb_loai.set("Chọn loại")  # Gán giá trị mặc định
    cmb_loai.grid(column=1, row=4, padx=10, pady=10)

    # Các nút hành động
    button_themsp = tk.Button(root, text="Thêm Sản phẩm", command=themsp, font=("Arial", 12))
    button_themsp.grid(column=0, row=5, sticky="nsew", padx=10, pady=20)

    button_capnhatsp = tk.Button(root, text="Cập Nhật Sản Phẩm", command=capnhatsp, font=("Arial", 12))
    button_capnhatsp.grid(column=1, row=5, sticky="nsew", padx=10, pady=20)

    button_ketxuat = tk.Button(root, text="Kết xuất", command=ketxuat, font=("Arial", 12))
    button_ketxuat.grid(column=2, row=5, sticky="nsew", padx=10, pady=20)
    
    button_reset = tk.Button(root,text="Reset",command=reset, font=("Arial",12))
    button_reset.grid(column=3,row=5,sticky="nsew" ,padx=10, pady=20)

    # Tạo Treeview để hiển thị dữ liệu
    global tree
    tree = ttk.Treeview(root, columns=("Mã Sản phẩm", "Tên Sản Phẩm", "Trọng Lượng", "Loại"), show="headings", height=10)
    tree.grid(column=0, row=6, columnspan=3, padx=20, pady=20)

    # Đặt tên và kích thước cột
    tree.heading("Mã Sản phẩm", text="Mã Sản phẩm")
    tree.column("Mã Sản phẩm", width=150)
    tree.heading("Tên Sản Phẩm", text="Tên Sản Phẩm")
    tree.column("Tên Sản Phẩm", width=200)
    tree.heading("Trọng Lượng", text="Trọng Lượng")
    tree.column("Trọng Lượng", width=120)
    tree.heading("Loại", text="Loại")
    tree.column("Loại", width=150)

    hienthiTree()  # Làm mới Treeview sau khi khởi động

# Các hàm xử lý hành động của các nút
def themsp():
    masp = entry_masp.get()
    tensp = entry_tensp.get()
    trongluong = entry_trongL.get()
    loai = cmb_loai.get()

    if not masp or not tensp or not trongluong or loai == "Chọn loại":
        messagebox.showerror("Lỗi nhập liệu", "Vui lòng điền đầy đủ thông tin!")
        return

    try:
        trongluong = float(trongluong)
    except ValueError:
        messagebox.showerror("Lỗi nhập liệu", "Trọng lượng phải là một số hợp lệ!")
        return

    conn = ketnoi_db()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO Test (masanpham, tensanpham, trongluong, loai)
        VALUES (masp, tensp, trongluong, loại)""")
        conn.commit()
        messagebox.showinfo("Thành công", "Thêm sản phẩm thành công!")
        hienthiTree()  # Làm mới Treeview sau khi thêm sản phẩm
    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi khi thêm sản phẩm: {e}")
    finally:
        conn.close()

def capnhatsp():
    masp = entry_masp.get()
    tensp = entry_tensp.get()
    trongluong = entry_trongL.get()
    loai = cmb_loai.get()

    if not masp or not tensp or not trongluong or loai == "Chọn loại":
        messagebox.showerror("Lỗi nhập liệu", "Vui lòng điền đầy đủ thông tin!")
        return

    try:
        trongluong = float(trongluong)
    except ValueError:
        messagebox.showerror("Lỗi nhập liệu", "Trọng lượng phải là một số hợp lệ!")
        return

    conn = ketnoi_db()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        sql = """
        UPDATE Test 
        SET tensanpham = ?, trongluong = ?, loai = ?
        WHERE masanpham = ?
        """
        cursor.execute(sql, tensp, trongluong, loai, masp)
        conn.commit()
        messagebox.showinfo("Thành công", "Cập nhật sản phẩm thành công!")
        hienthiTree()  # Làm mới Treeview sau khi cập nhật
    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi khi cập nhật sản phẩm: {e}")
    finally:
        conn.close()

def ketxuat():
    messagebox.showinfo("Thông báo", "Chức năng kết xuất chưa được triển khai.")
def reset():
    entry_masp.delete(0,tk.END)
    entry_tensp.delete(0,tk.END)
    entry_trongL.delete(0,tk.END)
    cmb_loai.set("Chọn loại")

# Hàm chính để chạy ứng dụng
def main():
    giaodienQL()
    root.mainloop()

# Chạy chương trình
main()
