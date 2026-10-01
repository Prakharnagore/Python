message = "a"


def greet():
    global message  # to modify the global variable
    message = "b"
    print(message)


greet()  # b
print(message)  # b , since global variable is modified using global keyword
