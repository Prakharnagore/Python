letters = ["a", "b", "c"]

# Add
letters.append("d")
print(letters)  # ['a', 'b', 'c', 'd']

# Insert
letters.insert(0, "-")
print(letters)  # ['-', 'a', 'b', 'c', 'd']

# Remove
letters.pop()
print(letters)  # ['-', 'a', 'b', 'c']

# Remove by index
letters.pop(0)
print(letters)  # ['a', 'c']

# Remove by value
letters.remove("b")  # removes the first occurrence of the value
print(letters)  # ['-', 'a', 'c']


# Delete by index
# syntax: del list[start:end]
del letters[0]
del letters[0:2]
print(letters)  # ['c']
