number = [1, 2, 3]
first, second, third = number
print(first, second, third)

# Error: ValueError: too many values to unpack (expected 2)
first, second = number

first, *other = number
print(other)  # [2, 3]

number = [1, 2, 3, 4, 5]
first, *other, last = number
print(other)  # [2, 3, 4]
print(first, last)  # 1 5
