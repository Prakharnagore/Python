try:
    age = int(input("Age: "))
    xfactor = 10 / age  # We cannot dvide number by 0 - It will give a ZeroDivisionError
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("Age cannot be 0")
else:
    print("No exceptions were thrown")
finally:
    print("Try block is finished")


# We can handle multiple exceptions in the same try block
try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("Invalid value")
else:
    print("No exceptions were thrown")
