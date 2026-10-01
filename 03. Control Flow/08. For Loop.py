for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")

# range(start, end, step) - start is inclusive, end is exclusive, step is the increment
for number in range(1, 4):
    print("Attempt", number, number * ".")

for number in range(1, 4, 2):
    print("Attempt", number, number * ".")
