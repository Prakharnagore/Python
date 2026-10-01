
prices = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

# map function
x = map(lambda item: item[1], prices)
print(prices)  # [10, 9, 12]

# filter function
x = filter(lambda item: item[1] >= 10, prices)
print(x)  # <filter object at 0x7f8968146400>

# List Comprehensions - Full syntax:
# [expression for item in items if condition]

prices = [item[1] for item in prices]
print(prices)  # [10, 9, 12]

prices = [item[1] for item in prices if item[1] >= 10]
print(prices)  # [10, 12]

# List Comprehensions
# [expression for item in items if condition]

prices = [item[1] for item in prices]
print(prices)  # [10, 9, 12]


prices = [item for item in prices if item[1] >= 10]
print(prices)  # [("Product1", 10), ("Product3", 12)]
