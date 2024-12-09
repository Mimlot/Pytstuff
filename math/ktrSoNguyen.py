def ktr(so):
    if (so.isdigit()):
        return True
    else:
        return False

while True:
    so = input("Nhap so nguyen: ")
    if ktr(so):
        break
    else:
        print("Số đó không phải là số nguyên")
        print("Vui lòng nhập số nguyên!")
        
print("Số đó là số nguyên")

    

    
