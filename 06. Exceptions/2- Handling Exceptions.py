try:
    age = int(input("Age: "))
except ValueError:
    print("Invalid value")
else:
    print("No exceptions were thrown")
finally:
    print("Try block is finished")
