# 1st programm
my_dict = {"Hello": "Hi", "One": 1, "spisok": [1, 2, 3, 4, 5]}
print(f"Dict: {my_dict}")
print(f"Existing value: {my_dict.get('Hello')}")
print(f'Not existing value: {my_dict.get("Two", "Dont exist")}')
my_dict["Goodbye"] = "Poka"
my_dict["Russia"] = "Россия"
keys = my_dict.pop("One")
print(f"Deleted value: {keys}")
print(f"Modified dictionary: {my_dict}")
print()

# 2nd programm

my_set = set([1, 2, 3, 4, 5, 4, 4, True, 0, 0, 0, "Hello", "Hello"])
print(f"Set: {my_set}")
my_set.update(["Urban"])
my_set.update(["Kazan"])
my_set.remove("Hello")
print(f"Modified set: {my_set}")
