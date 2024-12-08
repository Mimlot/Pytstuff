import pandas as pd


df = pd.read_csv("lmao2.csv")


column_name = input("Tên cột mới muốn thêm: ")


nam3li = []


for index, row in df.iterrows():
    nam3 = input(f"Nhập giá trị cho {row['nam1']} với thông tin là {row['nam2']}: ")
    nam3li.append(nam3)  


df[column_name] = nam3li


df.to_csv("lmao2.csv", index=False)

print("Đã thêm cột mới thành công!")
