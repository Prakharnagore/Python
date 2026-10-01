numbers = [3, 51, 2, 8, 1, 4]

# Sort the list in ascending order
numbers.sort()
print(numbers)  # [1, 2, 3, 4, 51, 8]

# Sort the list in descending order
numbers.sort(reverse=True)
print(numbers)  # [51, 8, 4, 3, 2, 1]

# sorted() function returns a new list, does not modify the original list like sort()
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 2, 3, 4, 51, 8]
print(numbers)  # [3, 51, 2, 8, 1, 4]

# reverse=True argument to sort() and sorted()
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)  # [51, 8, 4, 3, 2, 1]
print(numbers)  # [3, 51, 2, 8, 1, 4]


items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)  # [("Product2", 9), ("Product1", 10), ("Product3", 12)]
