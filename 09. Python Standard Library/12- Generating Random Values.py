import random
import string

print(random.random())  # 0.0 to 1.0
print(random.randint(1, 10))  # 1 to 10
print(random.choice([1, 2, 3, 4, 5]))  # 1, 2, 3, 4, 5
print(random.choices([1, 2, 3, 4, 5], k=2))  # [1, 2]
# ['a', 'b', 'c', 'd', 'e'] - random choice of 5 characters from the string
print(random.choices("abcdefghijklmnopqrstuvwxyz", k=5))


# 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(string.ascii_letters)
# '0123456789' - all digits
print(string.digits)
# 'abcdefghijklmnopqrstuvwxyz' - all lowercase letters
print(string.ascii_lowercase)
# 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' - all uppercase letters
print(string.ascii_uppercase)
# '0123456789' - all digits
print(string.digits)
# '0123456789' - all digits


print("".join(random.choices(string.ascii_letters + string.digits, k=6)))
print(random.shuffle([1, 2, 3, 4, 5]))
