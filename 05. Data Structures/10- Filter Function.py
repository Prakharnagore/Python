items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

x = filter(lambda item: item[1] >= 10, items)
print(x)  # <filter object at 0x7f8968146400>

for item in x:
    print(item)  # ("Product1", 10) ("Product3", 12)

print(list(x))  # [("Product1", 10), ("Product3", 12)]
