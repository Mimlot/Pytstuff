from collections import Counter

def count_num(day):
    #so =[i for i in day if i.isdigit()]
    dem = 0
    for i in day:
        if i.isdigit():
            dem += 1
    return dem
def count_words(day):
    return Counter(day)

def main ():
    day = list(input("Nhap day ky tu khac nhau : "))
    print(count_num(day))
    d = count_words(day)
    for i in d:
        print(f"{i} xuat hien {d[i]} lan")
main()