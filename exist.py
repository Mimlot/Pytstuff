


def lol(d,key):
    for key in d:
        if key in d:
            return True
    return False
d = {"name": "Alice", "age": 25, "city": "New York"}
key = input("nhap cai can tim: ")

print(lol(d,key))