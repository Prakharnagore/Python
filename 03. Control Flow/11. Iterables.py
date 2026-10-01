print(type(5))  # <class 'int'>
print(type(range(5)))  # <class 'range'>

# Complex Types that are iterable
# Range, String, List, Tuple, Dictionary, Set

# Range is iterable
for x in range(5):
    print(x)

# String is iterable
for x in "Python":
    print(x)

# List is iterable
for x in [1, 2, 3, 4, 5]:
    print(x)
