def swap(array, l, r):
    array[l], array[r] = array[r], array[l]


class Heap:
    def __init__(self):
        self.buffer = []

    def __sift_down(self, idx):
        left_idx = 2 * idx + 1
        right_idx = 2 * idx + 2
        largest_idx = idx
        if left_idx < len(self.buffer) and self.buffer[left_idx] > self.buffer[largest_idx]:
            largest_idx = left_idx
        if right_idx < len(self.buffer) and self.buffer[right_idx] > self.buffer[largest_idx]:
            largest_idx = right_idx
        if largest_idx != idx:
            swap(self.buffer, idx, largest_idx)
            self.__sift_down(largest_idx)

    def __sift_up(self, idx):
        while idx > 0:
            parent_idx = (idx - 1) // 2
            if self.buffer[idx] <= self.buffer[parent_idx]:
                return
            swap(self.buffer, idx, parent_idx)
            idx = parent_idx

    def add(self, element):
        self.buffer.append(element)
        self.__sift_up(len(self.buffer) - 1)

    def build(self, array):
        self.buffer = array
        for i in range(len(self.buffer) // 2 - 1, 0, -1):
            self.__sift_down(i)

    def top(self):
        return self.buffer[0]

    def pop(self):
        if not self.buffer:
            return None
        swap(self.buffer, 0, len(self.buffer) - 1)
        result = self.buffer.pop(-1)

        if self.buffer:
            self.__sift_down(0)

        return result
