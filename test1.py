def max(max, list):
    for i in list:
        if i > max:
            max = i
    return max
def main():
    numbers = list(map(int, input("Number of numbers : ").split()))
    print("The maximum number is ", max(0, numbers))
main()