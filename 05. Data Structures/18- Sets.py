number = [1, 1, 2, 3, 4]
type(number)  # list
first = set(number)
second = {1, 4}
type(second)  # set
print(first)

first.add(5)
first.remove(3)
first.clear()
print(first)

second.add(5)
second.remove(4)
second.clear()
print(second)


# Union - returns a new set with all elements from both sets without duplicates.
print(first | second)
# Intersection - returns a new set with elements that are in both sets.
print(first & second)
# Difference - returns a new set with elements that are in the first set but not in the second set.
print(first - second)
# Difference - returns a new set with elements that are in the second set but not in the first set.
print(second - first)
# Symmetric Difference - returns a new set with elements that are in either set but not in both.
print(first ^ second)


# This will raise an error because sets are unordered. We cannot access elements by index.
# print(first[0])


if 1 in first:
    print("Yes")
else:
    print("No")
