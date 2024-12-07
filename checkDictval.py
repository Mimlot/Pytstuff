d = {"name": "Alice", "age": None, "city": "New York", "hobby": None}
for key, value in list(d.items()):
    if value is None:
        d.pop(key)
print(d)