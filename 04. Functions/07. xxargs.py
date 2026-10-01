def save_user(**user):
    print(user)  # return a dictionary - {'id': 1, 'name': 'John', 'age': 20}
    print(user["id"])


save_user(id=1, name="John", age=20)
