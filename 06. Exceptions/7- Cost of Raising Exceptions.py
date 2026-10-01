from timeit import timeit

code1 = """ 
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age

def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age
"""

# Runs the code 10000 times and returns the time it took to run
print("first_code: ", timeit(code1, 10000))
