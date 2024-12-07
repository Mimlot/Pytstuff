from collections import Counter

def dem_so_nguyen(day_so):
    dem = Counter(day_so)
    return dem
def tinh_so_le(day_so):
    so_le = 0
    for num in day_so:
        if num % 2 != 0:
            so_le += 1
    tong = len(day_so)
    ty_le_le = (so_le / tong) * 100
    return ty_le_le

day_so = [1, 2, 3, 4, 2, 5, 6, 3]
print(f"Cac so nguyen xuat hien 2 lan tro len : {dem_so_nguyen(day_so)}")
print(f"Ti le so le xuat hien la {tinh_so_le(day_so)}%")

