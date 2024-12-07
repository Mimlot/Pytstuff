def nhap_diem():
    while True:
        m = int(input("Nhập số sinh viên (10 <= m <= 30): "))
        if 10 <= m <= 30:
            break
        print("Số sinh viên phải từ 10 đến 30. Hãy nhập lại!")

    while True:
        n = int(input("Nhập số môn học (5 <= n <= 10): "))
        if 5 <= n <= 10:
            break
        print("Số môn học phải từ 5 đến 10. Hãy nhập lại!")
        
    diem_sv = {}

    for i in range(1, m+1):
        ten_sv = input(f"Nhập tên sinh viên {i}: ")
        diem = []

        for j in range(1, n+1):
            diem_mon = float(input(f"Nhập điểm môn {j} của {ten_sv}: "))
            diem.append(diem_mon)
            
        diem_sv[ten_sv] = diem
    
    return diem_sv
def hien_thi_diem(diem_sinh_vien):
    print("--- Danh sách điểm sinh viên ---")
    for ten, diem in diem_sinh_vien.items():
        print(f"Sinh viên: {ten}, Điểm các môn: {diem}")
def tinh_diem_TB(diem_sinh_vien):
    diem_tb_sv = {}
    print("--- Điểm trung bình của mỗi sinh viên ---")
    for ten, diem in diem_sinh_vien.items():
        diem_tb = sum(diem) / len(diem)
        diem_tb_sv[ten] = diem_tb
        print(f"Sinh viên: {ten}, Điểm trung bình: {diem_tb:.2f}")
    
    return diem_tb_sv

def xep_thu_hang_sv(diem_tb_sv):
    print("--- Xếp hạng sinh viên theo điểm trung bình ---")
    diem_sv_sorted = sorted(diem_tb_sv.items(), key=lambda x: sum(x[1]) / len(x[1]), reverse=True)
    
    hang = 1
    diem_truoc = -1
    dong_hang = 1
    
    print("--- Xếp hạng sinh viên ---")
    for i, (ten, diem) in enumerate(diem_sv_sorted):
        diem_tb = sum(diem) / len(diem)  
        if diem_tb != diem_truoc:
            hang = i + 1
            dong_hang = hang
        else:
            hang = dong_hang  
        
        print(f"Hạng {hang}: {ten}, Điểm trung bình: {diem_tb:.2f}")
        diem_truoc = diem_tb
def tim_sv_gioi_nhat_va_kem_nhat(diem_tb_sv):
    diem_tb_sv = {ten: sum(diem) / len(diem) for ten, diem in diem_tb_sv.items()}
    sv_gioi_nhat = max(diem_tb_sv, key=diem_tb_sv.get)
    sv_kem_nhat = min(diem_tb_sv, key=diem_tb_sv.get)
    print(f"Sinh viên giỏi nhất: {sv_gioi_nhat}, Điểm trung bình: {diem_tb_sv[sv_gioi_nhat]:.2f}")
    print(f"Sinh viên kém nhất: {sv_kem_nhat}, Điểm trung bình: {diem_tb_sv[sv_kem_nhat]:.2f}")

def thong_ke_phan_loai(diem_tb_sv):
    
    gioi = 0
    kha = 0
    trung_binh = 0
    yeu = 0
    diem_tb_sv= {ten: sum(diem) / len(diem) for ten, diem in diem_tb_sv.items()}
    for diem_tb in diem_tb_sv.values():
        if diem_tb >= 8.0:
            gioi += 1
        elif diem_tb >= 6.0:
            kha += 1
        elif diem_tb >= 5.0:
            trung_binh += 1
        else:
            yeu += 1
    
    print("--- Thống kê số lượng sinh viên theo học lực ---")
    print(f"Số lượng sinh viên giỏi: {gioi}")
    print(f"Số lượng sinh viên khá: {kha}")
    print(f"Số lượng sinh viên trung bình: {trung_binh}")
    print(f"Số lượng sinh viên yếu: {yeu}")
           
diem_sinh_vien = nhap_diem()
hien_thi_diem(diem_sinh_vien)
tinh_diem_TB(diem_sinh_vien)
xep_thu_hang_sv(diem_sinh_vien)
tim_sv_gioi_nhat_va_kem_nhat(diem_sinh_vien)
thong_ke_phan_loai(diem_sinh_vien)