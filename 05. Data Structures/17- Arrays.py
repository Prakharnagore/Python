from array import array

# Here "i" is the type code for integers.
# There are other type codes for other types of data.
# "i" is the type code for integers.
# "f" is the type code for floats.
# "d" is the type code for doubles.
# "c" is the type code for characters.
# "b" is the type code for bytes.
# "h" is the type code for short integers.
# "l" is the type code for long integers.
# "q" is the type code for long long integers.
# "f" is the type code for floats.
# Check the documentation for more type codes.
# "https://docs.python.org/3/library/array.html"

# syntax: array(typecode, [initial values])

numbers = array("i", [1, 2, 3])

numbers.append(4)
numbers.append(4)
numbers.append(4)
numbers.insert(0, 0)
numbers.pop()
numbers.remove(2)
# This will raise an error because the array is of type integers.
numbers[0] = 1.0
