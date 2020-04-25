def array_diff(a,b):
    temp = []
    for element in a:
        if element not in b:
            temp.append(element)
    return temp