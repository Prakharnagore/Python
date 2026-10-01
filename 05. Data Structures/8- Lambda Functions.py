# Syntax of a lambda function:

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

# Syntax of a lambda function (anonymous function): lambda parameters: expression
items.sort(key=lambda item: item[1])
print(items)  # [("Product2", 9), ("Product1", 10), ("Product3", 12)]
