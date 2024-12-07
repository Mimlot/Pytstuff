def count(ds,pt):
    soLan=ds.count(pt)
    return soLan
user_inputs=[]
num_input= int(input("Nhap so luong so trong danh sach: "))

for i in range(num_input):
    user_input = int(input(f"Enter input {i + 1}: "))
    user_inputs.append(user_input)

findNum = int(input("nhap so ban can tim: "))
print(f"So lan xuat hien cua {findNum} trong danh sach la: {count(user_inputs,findNum)}")