ok = "oubfnakiufb"
dem = list(ok)
soluong = {}
for char in dem:
    if char in soluong:
        soluong[char] +=1
    else:
        soluong[char]=1
print(soluong)