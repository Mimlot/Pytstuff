from collections import Counter
def XuathienKT(st):
    return Counter(st)

while True:
    st = input("Nhập một chuỗi")
    if len(st)>= 5 and len(st)<=10:
        break
    else:
        print("Yêu cầu nhập lại!")
#hiển thị
print("Tổng hợp sự xuất hiện của ký tự trong ", st)
d = XuathienKT(st)
for i in d:
    print(i, 'xuất hiện ', d[i],' lần')