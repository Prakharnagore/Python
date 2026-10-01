# Dictionary Comprehensions

values = [x*2 for x in range(5)]
print(values)  # [0, 2, 4, 6, 8]

values = {x: x*2 for x in range(5)}
print(values)  # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

values = {x: x*2 for x in range(5) if x % 2 == 0}
print(values)  # {0: 0, 2: 4, 4: 8}

values = {x: x*2 for x in range(5) if x % 2 != 0}
print(values)  # {1: 2, 3: 6}


# Tuple Comprehensions
values = (x*2 for x in range(5))
print(values)  # <generator object <genexpr> at 0x7f9c5c0a0a00>
