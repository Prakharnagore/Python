age = 17
if age >= 18:
    message = "Eligible"
else:
    message = "Not eligible"
print(message)

# Ternary Operator
message = "Eligible" if age >= 18 else "Not eligible"
print(message)

# Nested Ternary Operator
age = 20
message = "Invalid" if age < 0 else "Eligible" if age >= 18 else "Not eligible"
print(message)
