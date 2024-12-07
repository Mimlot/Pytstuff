def so():
 n = int(input("Nhap vao so luong: "))
 for i in range(1,n+1):
    for j in range(i+1):
        print(j, end=" ")
    print()