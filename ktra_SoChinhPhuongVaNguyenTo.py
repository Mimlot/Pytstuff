import math

def la_so_chinh_phuong(n):
    if n < 0:
        return False
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def hien_thi(nums):
    so_chinh_phuong = []
    so_nguyen_to = []
    
    for num in nums:
        if la_so_chinh_phuong(num):
            so_chinh_phuong.append(num)
        if la_so_nguyen_to(num):
            so_nguyen_to.append(num)
    
    print(f"Số lượng số chính phương: {len(so_chinh_phuong)}")
    print(f"Các số chính phương: {so_chinh_phuong}")
    
    print(f"Số lượng số nguyên tố: {len(so_nguyen_to)}")
    print(f"Các số nguyên tố: {so_nguyen_to}")

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 16, 17, 18, 19, 20]
hien_thi(nums)