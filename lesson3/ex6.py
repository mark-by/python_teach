import datetime
def lin_serach(array, element):
    for i in range(len(array)):
        if (array[i] == element):
            return i
    return -1

a = [i for i in range(100000000)]

start = datetime.datetime.now()
print(lin_serach(a, 99999999))
print((start - datetime.datetime.now()).seconds)
