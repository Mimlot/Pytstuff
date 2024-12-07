def nguoc(list):
    return list[::-1]
def main():
    nhap= input("Please nhap: ")
    print(f"chuoi dao nguoc: {nguoc(nhap)}")
main()