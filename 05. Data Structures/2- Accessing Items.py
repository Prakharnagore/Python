letters = ["a", "b", "c"]

# syntax
# list[start:end:step] - end is not included

print(letters[0])  # a
print(letters[-1])  # c
print(letters[0:3])  # ['a', 'b', 'c']
print(letters[::2])  # ['a', 'c']
print(letters[::-1])  # ['c', 'b', 'a']
print(letters[::-2])  # ['c', 'a']
print(letters[::-3])  # ['c']
print(letters[::-4])  # ['c']


numbers = list(range(20))
print(numbers[::2])  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
