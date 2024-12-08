def perfect_nums(so):
    if so <1 :
        return False
    else:
        perfect = [i for i in range(1, so) if i % so == 0]
        if sum(perfect) == 0 :
            return True
        else:
            return False
def main():
    so = int(input("Nhap so : "))
    if perfect_nums(so):
        print(f"{so} la so hoan hao")
    else:
        print(f"{so} khong phai la so hoan hao")
main()