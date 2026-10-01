numbers = [1, 2, 3]
print(*numbers)  # 1,2,3


values = list(range(3))
values = [*range(3)]
print(values)  # [0, 1, 2]

values = [*range(3), *"Hello"]
print(values)  # [0, 1, 2, 'H', 'e', 'l', 'l', 'o']

first = [1, 2]
second = [3]
values = [*first, *second]
print(values)  # [1, 2, 3]


first = {"x": 1}
second = {"x": 10, "y": 2}
values = {**first, **second}
print(values)  # {'x': 10, 'y': 2}

# difference between xargs and xxargs
# xargs is used to pass a variable number of arguments to a function
# xxargs is used to pass a variable number of arguments to a function as a dictionary
