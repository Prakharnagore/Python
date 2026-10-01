try:
    file = open("app.py")
    age = int(input("Age: "))
    xfactor = 10 / age
except FileNotFoundError:
    print("File not found")
else:
    print(file.read())
finally:
    file.close()
