import tkinter as tk
from tkinter import ttk, messagebox


# Lớp chính để quản lý các tòa nhà
class BuildingManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản lý tòa nhà trường đại học")
        self.root.geometry("600x400")

        # Danh sách lưu thông tin các tòa nhà
        self.buildings = []

        # Tạo giao diện
        self.create_widgets()

    def create_widgets(self):
        # Frame nhập liệu
        input_frame = tk.LabelFrame(self.root, text="Nhập thông tin tòa nhà", padx=10, pady=10)
        input_frame.pack()

        # Tên tòa nhà
        tk.Label(input_frame, text="Tên tòa nhà:").grid(row=0, column=0, sticky="w", pady=5)
        self.name_entry = tk.Entry(input_frame, width=30)
        self.name_entry.grid(row=0, column=1, pady=5)

        # Số lượng tầng
        tk.Label(input_frame, text="Số lượng tầng:").grid(row=1, column=0, sticky="w", pady=5)
        self.floors_entry = tk.Entry(input_frame, width=30)
        self.floors_entry.grid(row=1, column=1, pady=5)

        # Số lượng phòng
        tk.Label(input_frame, text="Số lượng phòng:").grid(row=2, column=0, sticky="w", pady=5)
        self.rooms_entry = tk.Entry(input_frame, width=30)
        self.rooms_entry.grid(row=2, column=1, pady=5)

        # Người quản lý
        tk.Label(input_frame, text="Người quản lý:").grid(row=3, column=0, sticky="w", pady=5)
        self.manager_entry = tk.Entry(input_frame, width=30)
        self.manager_entry.grid(row=3, column=1, pady=5)

        # Nút thêm tòa nhà
        add_button = tk.Button(input_frame, text="Thêm tòa nhà", command=self.add_building)
        add_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Frame hiển thị danh sách tòa nhà
        display_frame = tk.LabelFrame(self.root, text="Danh sách tòa nhà", padx=10, pady=10)
        display_frame.pack(fill="both", padx=10, pady=10, expand=True)

        # Treeview để hiển thị danh sách tòa nhà
        columns = ("name", "floors", "rooms", "manager")
        self.building_tree = ttk.Treeview(display_frame, columns=columns, show="headings")
        self.building_tree.heading("name", text="Tên tòa nhà")
        self.building_tree.heading("floors", text="Số tầng")
        self.building_tree.heading("rooms", text="Số phòng")
        self.building_tree.heading("manager", text="Người quản lý")
        self.building_tree.pack(fill="both", expand=True)

    def add_building(self):
        # Lấy dữ liệu từ các ô nhập liệu
        name = self.name_entry.get().strip()
        floors = self.floors_entry.get().strip()
        rooms = self.rooms_entry.get().strip()
        manager = self.manager_entry.get().strip()

        # Kiểm tra đầu vào
        if not name or not floors or not rooms or not manager:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        try:
            floors = int(floors)
            rooms = int(rooms)
        except ValueError:
            messagebox.showerror("Lỗi", "Số lượng tầng và phòng phải là số nguyên!")
            return

        # Lưu thông tin vào danh sách
        building_info = {"name": name, "floors": floors, "rooms": rooms, "manager": manager}
        self.buildings.append(building_info)

        # Cập nhật Treeview
        self.building_tree.insert("", "end", values=(name, floors, rooms, manager))

        # Xóa các ô nhập liệu
        self.clear_inputs()

        # Hiển thị thông báo
        messagebox.showinfo("Thành công", "Đã thêm tòa nhà thành công!")

    def clear_inputs(self):
        # Xóa dữ liệu trong các ô nhập
        self.name_entry.delete(0, tk.END)
        self.floors_entry.delete(0, tk.END)
        self.rooms_entry.delete(0, tk.END)
        self.manager_entry.delete(0, tk.END)


# Chạy ứng dụng
if __name__ == "__main__":
    root = tk.Tk()
    app = BuildingManagerApp(root)
    root.mainloop()
