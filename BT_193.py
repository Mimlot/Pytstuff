import math
from functools import reduce


def find_gcd(arr):
    return reduce(math.gcd, arr)


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def find_lcm(arr):
    return reduce(lcm, arr)


n = int(input("Nhập số phần tử trong danh sách: "))
arr = [int(input(f"Nhập số nguyên thứ {i+1}: ")) for i in range(n)]


gcd_value = find_gcd(arr)
lcm_value = find_lcm(arr)

print("Ước chung lớn nhất của dãy:", gcd_value)
print("Bội chung nhỏ nhất của dãy:", lcm_value)
