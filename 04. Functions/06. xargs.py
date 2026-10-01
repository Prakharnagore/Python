def multiply(*numbers):
    print(numbers)  # return a tuple - (2, 3, 4, 5)
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))  # 120
