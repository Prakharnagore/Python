try:
    with open("app.py") as file:
        print("File opened.")
    age = int(input("Age: "))
    xfactor = 10 / age
except FileNotFoundError:
    print("File not found")
else:
    print(file.read())
finally:
    file.close()


try:
    with open("app.py") as file, open("app.txt") as target:
        print("File opened.")
    age = int(input("Age: "))
    xfactor = 10 / age
except FileNotFoundError:
    print("File not found")
else:
    print(file.read())
finally:
    file.close()
