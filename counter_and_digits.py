from collections import Counter

def count_num(day):
    so =[i for i in day if i.isdigit()]
    return so
def count_words(day):
    return Counter(day)

def main ():
    day = list(input("Nhap day ky tu khac nhau : "))
    print(count_num(day))
    print(count_words(day))
main()