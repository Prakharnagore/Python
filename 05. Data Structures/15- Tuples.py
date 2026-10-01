# Tuples are immutable sequences of objects.

point = (1, 2)
print(type(point)) 

point = 1, 2
print(type(point))

point = 1,
print(type(point))

point = ()
print(type(point))


point = (1, 2) + (3, 4)
print(point)


point = (1, 2) * 3 
print(point) 

point = tuple([1, 2])
print(point)

point = tuple("Hello")
print(point) 
