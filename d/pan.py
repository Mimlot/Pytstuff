import pandas as pd

# Đọc file CSV
df = pd.read_csv("lmao2.csv")

# Nhập tên cột mới từ bàn phím
column_name = input("Tên cột mới muốn thêm: ")

# Tạo danh sách để lưu giá trị mới
nam3li = []

# Duyệt qua từng dòng và nhập giá trị
for index, row in df.iterrows():
    nam3 = input(f"Nhập giá trị cho {row['nam1']} với thông tin là {row['nam2']}: ")
    nam3li.append(nam3)  


df[column_name] = nam3li


df.to_csv("lmao2.csv", index=False)

print("Đã thêm cột mới thành công!")
