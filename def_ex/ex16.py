def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a = 1)
# {'a': 1}

print_kwargs(name = 'cherry', age = 3)
# {'name': 'cherry', 'age': 3}

