<<<<<<< HEAD
#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            copy.append(replace)
        else:
            copy.append(my_list[i])
    return copy
=======
#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            copy.append(replace)
        else:
            copy.append(my_list[i])
    return copy
>>>>>>> c1c5f9e6cde8cfee0f0e8fc4ec33c45207945bcc
