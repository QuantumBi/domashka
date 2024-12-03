def print_params(a = 1, b = "строка", c = True):
    print(a, b, c)

print_params()
print_params(3)
print_params("Kek", False)

print("-"*15)

print_params(b = 25)
print_params(c = [1,2,3])

print("-"*15)

value_list = ["Urban", 2024, False]
value_dict = {"a": "ne stroka", "b": [True, False, True], "c": 666}

print_params(*value_list)
print_params(**value_dict)

print("-"*15)

values_list_2 = [0, "Study"]
print_params(*values_list_2, 42)

