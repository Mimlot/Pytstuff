cau = "python is fun and python is easy"
dem = cau.split()
soluong = {}
for i in dem:
    if i in soluong: 
        soluong[i] += 1
    else:
        soluong[i] = 1
print(soluong)