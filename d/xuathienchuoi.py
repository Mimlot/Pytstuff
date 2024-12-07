from collections import Counter 
def xuat(st):
   return Counter(st)
while True:
    st = input("nhap 1 chuoi : " )
    if len(st) >= 5 and len(st) <= 10:
        break
    else:
        print("chuoi phai co do dai tu 6 den 9 ky tu")
d = xuat(st)
for i in d:
    print(i ,f" appears {d[i]} times")