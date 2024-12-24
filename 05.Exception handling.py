try:
    my_dict = {"name": "Alice", "age": 25}
    print(my_dict["address"])
except KeyError:
    print("Key not found in dictionary.")
