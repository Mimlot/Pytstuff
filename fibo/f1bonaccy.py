def fibo(n):
    f0,f1 = 0,1
    for i in range(1,n):
        fn = f0+f1
        f0= f1
        f1 =fn
    return fn
def main():
    n = int(input("nhap n : "))
    print(f"{fibo(n)}")
main()