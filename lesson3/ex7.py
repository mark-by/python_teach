import datetime

def lin_search(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return i
    return -1

def bin_search(array, element):
    start_idx = 0
    end_idx = len(array)

    while start_idx < end_idx:
        mid = (start_idx + end_idx) // 2
        guess = array[mid]
        if guess == element:
            return mid
        if guess < element:
            start_idx = mid + 1
        else:
            end_idx = mid
    return -1


print("creating list...")
a = [i for i in range(100000000)]
b = [i for i in range(100000000)]
print("list creared")

start_bin = datetime.datetime.now()
x = bin_search(a, 99999999)
end_bin = datetime.datetime.now()
diff_bin = start_bin - end_bin

start_lin = datetime.datetime.now()
c = lin_search(b, 99999999)
end_lin = datetime.datetime.now()
diff_lin = start_lin - end_lin
print(f"BIN: {diff_bin.seconds}")
print(f"LIN: {diff_lin.seconds}")
