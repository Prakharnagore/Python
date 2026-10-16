# Dictionary is a unordered collection of key-value pairs

point = {"x": 1, "y": 2}
print(point)
print(type(point))  # <class 'dict'>

point = dict[str, int](x=1, y=2)
print(point)

point["x"] = 10
point["z"] = 30

point["x"]  # 10
point["y"]  # 2
point["a"]  # KeyError: 'a'


point.get("a")  # None
point.get("a", 0)  # 0 - If not a then return 0


del point["x"]

# Iterating over a dictionary
for key in point:
    print(key, point[key])

for key in point.items():
    print(key)  # (x, 10) (y, 2) (z, 30) - tuple

for key, value in point.items():
    print(key, value)

for x in point.values():
    print(x)

for x in point.keys():
    print(x)
