def sap_xep_day(lua_chon,day_so):
    
    if lua_chon == 1:
        day_so.sort()  
        print("Dãy số sau khi sắp xếp tăng dần:", day_so)
    elif lua_chon == 2:
        day_so.sort(reverse=True)  
        print("Dãy số sau khi sắp xếp giảm dần:", day_so)
    else:
        print("Lựa chọn không hợp lệ. Chỉ nhập 1 hoặc 2")

day_so = list(map(int, input("Nhập dãy số nguyên, cách nhau bởi dấu cách: ").split()))
lua_chon = int(input("Nhập '1' để sắp xếp tăng dần, '2' để sắp xếp giảm dần: "))
sap_xep_day(lua_chon,day_so)