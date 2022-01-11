def remove_elements(my_set):
    while my_set:
        my_set.pop()
        print(my_set)
my_set = set([12, 34, 45, 56, 67, 78])
remove_elements(my_set)