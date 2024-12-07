so = []
n = int(input("Nhap so luong so: "))
for i in range(n):
    so.append(int(input(f"Nhap so thu {i+1}: ")))
so_duong = 0
for num in so:
    if(num > 0):
        so_duong+=1
print(so_duong)