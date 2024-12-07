def chan(day):
    le = ""
    for i in range(len(day)):
        if int(day[i]) % 2 != 0:
            le += day[i]
        elif int(day[i]) % 2 == 0 and int(day[i + 1]) % 2 == 0:
            break
    return le


def main():
    while True:
        day = input("Nhập chuỗi các ký tự (ít nhất 10 ký tự): ")
        if len(day) >= 10: 
            break
        print("Vui lòng nhập ít nhất 10 số!")

    print("day so le : ", chan(day))

main()
