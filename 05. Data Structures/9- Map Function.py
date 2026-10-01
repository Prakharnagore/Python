items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

x = map(lambda item: item[1], items)
print(x)  # <map object at 0x7f8968146400>

for item in x:
    print(item)  # 10 9 12

print(list(x))  # [10, 9, 12]
