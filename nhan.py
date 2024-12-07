
def nhap_so(n):
    so = []
    for i in range(n):
        so.append(int(input(f"Nhap so thu {i+1} ")))
    return so
def nhan(so):
    if not so:
        return 0
    tich = 1
    for i in so:
        tich *= i
    return tich
n = int(input("nhap so luong: "))
so = nhap_so(n)
print(nhan(so))
    