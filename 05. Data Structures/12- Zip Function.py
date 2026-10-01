list1 = [1, 2, 3]
list2 = [10, 20, 30]

# zip function
# Example: 1
zipped = zip(list1, list2)
print(zipped)  # <zip object at 0x7f8968146400>

for item in zipped:
    print(item)  # (1, 10) (2, 20) (3, 30)

print(list(zipped))  # [(1, 10), (2, 20), (3, 30)]

# Example: 2
zipped = zip("abc", list1, list2)
print(zipped)  # <zip object at 0x7f8968146400>
print(list(zipped))  # [('a', 1, 10), ('b', 2, 20), ('c', 3, 30)]
