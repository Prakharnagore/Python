import sys

print(sys.argv)  # ['script.py', 'arg1', 'arg2', 'arg3']

if len(sys.argv) == 1:
    print("Usage: python script.py <password>")
else:
    password = sys.argv[1]
    print(password)
