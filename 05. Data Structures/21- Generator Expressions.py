from sys import getsizeof

# Tuple Comprehensions
values = (x*2 for x in range(5))
print(values)  # <generator object <genexpr> at 0x7f9c5c0a0a00>
print(len(values))  # error object of type 'generator' has no len()

# Get the size of the generator expression
values = (x*2 for x in range(1000000))
# 104 - 104 bytes for the generator expression - smaller memory usage
print(getsizeof(values))

values = [x*2 for x in range(1000000)]
# 800744 - 800744 bytes for the list - larger memory usage
print(getsizeof(values))
