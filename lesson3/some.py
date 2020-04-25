from datetime import datetime

def bin_search(array, element):
    start = 0
    end = len(array)
    while start < end:
        mid = (start + end) // 2
        if array[mid] < element:
            start = mid + 1
        else:
            end = mid
    if start == len(array) or array[start] != element:
        return None
    return start

def linear_search(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return i
    return None

arr = [i for i in range(100000000)]

start = datetime.now()
print(bin_search(arr, 99999999))
print(f"Bin search: {datetime.now() - start }")

start = datetime.now()
print(linear_search(arr, 99999999))
print(f"Linear search: {datetime.now() - start }")
