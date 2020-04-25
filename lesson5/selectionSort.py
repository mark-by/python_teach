def min_idx(arr):
    minimal = arr[0]
    minimal_idx = 0
    for index, element in enumerate(arr):
        if element < minimal:
            minimal = element
            minimal_idx = index
    return minimal_idx


def max_idx(arr):
    maximal = arr[0]
    maximal_idx = 0
    for index, element in enumerate(arr):
        if element > maximal:
            maximal = element
            maximal_idx = index
    return maximal_idx


def min_idx_in(arr, first, last):
    minimal = arr[first]
    minimal_idx = first
    for index in range(first, last):
        if arr[index] < minimal:
            minimal = arr[index]
            minimal_idx = index
    return minimal_idx


def selection_simple_sort(arr):
    new_array = []
    for i in range(len(arr)):
        minimal = min_idx(arr)
        new_array.append(arr.pop(minimal))
    return new_array


def selection_sort(arr):
    curr_idx = 0
    size = len(arr)
    while curr_idx < size:
        minimal_idx = min_idx_in(arr, curr_idx, size)
        arr[minimal_idx], arr[curr_idx] = arr[curr_idx], arr[minimal_idx]
        curr_idx += 1


def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

