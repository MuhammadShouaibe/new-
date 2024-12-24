try:
    my_list = [1, 2, 3]
    my_list.append(4)
    my_list.non_existent_method()
except AttributeError:
    print("Object does not have the specified method.")
